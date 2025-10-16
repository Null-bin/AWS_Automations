import boto3
from botocore.exceptions import ClientError

def analyze_s3_buckets():
    """
    Scaneia todos os buckets S3 em uma conta AWS e verifica configurações de acesso público.
    """
    s3_client = boto3.client('s3')
    print("Iniciando varredura de buckets S3...")

    try:
        response = s3_client.list_buckets()
    except ClientError as e:
        print(f"Erro ao listar buckets: {e}")
        return

    if not response['Buckets']:
        print("Nenhum bucket encontrado na conta.")
        return

    # Itera sobre cada bucket encontrado
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        is_public = False
        reason = ""

        # --- Verificação 1: Bloco de Acesso Público (Moderno) ---
        try:
            pab_status = s3_client.get_public_access_block(Bucket=bucket_name)
            # Se todas as configurações de bloqueio estiverem como False, pode ser público
            if not all(pab_status['PublicAccessBlockConfiguration'].values()):
                is_public = True
                reason += "[Alerta: Bloco de Acesso Público não está totalmente ativado] "
        except ClientError as e:
            # Se não houver configuração de PAB, é um sinal de alerta
            if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
                is_public = True
                reason += "[Alerta: NENHUM Bloco de Acesso Público configurado] "
            else:
                print(f"  Erro ao verificar PAB para o bucket {bucket_name}: {e}")

        # --- Verificação 2: Listas de Controle de Acesso (ACLs - Legado) ---
        try:
            acl = s3_client.get_bucket_acl(Bucket=bucket_name)
            for grant in acl['Grants']:
                grantee = grant.get('Grantee', {})
                # Verifica se o acesso é para 'Todos' ou 'Qualquer usuário autenticado na AWS'
                if 'URI' in grantee and ('AllUsers' in grantee['URI'] or 'AuthenticatedUsers' in grantee['URI']):
                    is_public = True
                    reason += f"[Alerta: ACL concede acesso a {grantee['URI'].split('/')[-1]}] "
                    break
        except ClientError as e:
            print(f"  Erro ao verificar ACL para o bucket {bucket_name}: {e}")

        # --- Imprime o resultado ---
        if is_public:
            print(f"🔴 BUCKET PÚBLICO: {bucket_name} | Motivo: {reason}")
        else:
            print(f"🟢 BUCKET SEGURO: {bucket_name}")

if __name__ == "__main__":
    analyze_s3_buckets()

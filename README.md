# AWS S3 Bucket Security Scanner 🛡️

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Um script de linha de comando em Python para auditar a segurança de buckets S3 em uma conta AWS, identificando configurações que podem levar à exposição pública de dados.

## 🎯 O Problema

Buckets S3 mal configurados são uma das causas mais comuns de vazamento de dados na nuvem. Um simples erro ao aplicar permissões pode expor arquivos sensíveis a qualquer pessoa na internet. Realizar auditorias manuais em dezenas ou centenas de buckets é um processo lento e sujeito a falhas.

Este projeto nasceu da necessidade de automatizar essa verificação, fornecendo um relatório rápido e claro sobre o estado de segurança dos buckets S3 de uma conta.

## ✨ Funcionalidades (Features)

* **Listagem Automática:** Conecta-se à sua conta AWS e lista todos os buckets S3 existentes.
  
* **Análise de Bloco de Acesso Público (PAB):** Verifica se o *Public Access Block*, a principal camada de proteção moderna da AWS, está corretamente configurado para cada bucket.
  
* **Análise de Listas de Controle de Acesso (ACLs):** Inspeciona as ACLs (método legado) para identificar permissões perigosas concedidas a grupos como `AllUsers` ou `AuthenticatedUsers`.
  
* **Relatório Intuitivo:** Exibe um output claro no terminal, usando cores para diferenciar buckets seguros (🟢) de buckets com potenciais falhas de configuração (🔴).

## Demonstração

**Exemplo de Saída no Terminal:**
![Exemplo de output do S3 Scanner](https://i.imgur.com/example.png)  

Iniciando varredura de buckets S3...

🟢 BUCKET SEGURO: meu-bucket-privado-corp

🟢 BUCKET SEGURO: logs-da-aplicacao-seguros

🔴 BUCKET PÚBLICO: meu-site-estatico-publico | Motivo: [Alerta: ACL concede acesso a AllUsers]

🔴 BUCKET PÚBLICO: bucket-com-erro-config | Motivo: [Alerta: NENHUM Bloco de Acesso Público configurado]

### 🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal do projeto.

Boto3: A SDK oficial da AWS para Python, usada para interagir com a API do S3.

AWS CLI: Necessária para a configuração inicial das credenciais de acesso à AWS.

### ⚙️ Pré-requisitos e Instalação
Antes de começar, você precisa ter o Python 3, a AWS CLI e as suas credenciais da AWS configuradas.

#### 1-Clone o repositório:
git clone [https://github.com/](https://github.com/)Null-bin/Null-bin.git
cd AWS_Automations

#### 2-(Opcional, mas recomendado) Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

#### 3-Instale as dependências:
pip install -r requirements.txt
(Certifique-se de ter um arquivo requirements.txt com boto3 dentro dele).

#### 4-Configure suas credenciais AWS: Se ainda não tiver feito, configure suas credenciais de acesso. O script usará as mesmas credenciais.
aws configure

### 🚀 Como Executar
Para rodar o scanner, simplesmente execute o script principal:
O script irá autenticar-se automaticamente usando suas credenciais configuradas e começará a análise, imprimindo os resultados diretamente no seu terminal.

#### 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

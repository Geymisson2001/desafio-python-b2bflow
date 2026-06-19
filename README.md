# Desafio Técnico - Estágio em Desenvolvimento Python (b2bflow)

Este repositório contém a resolução do desafio técnico para a vaga de Estágio em Desenvolvimento Python na b2bflow. O objetivo do projeto é ler contatos cadastrados em um banco de dados Supabase e disparar mensagens personalizadas via WhatsApp utilizando a Z-API.

## Funcionalidades
* Integração nativa com banco de dados PostgreSQL via Supabase.
* Disparo automatizado e personalizado de mensagens via Z-API.
* Tratamento de erros estruturado (o fluxo não quebra se um número falhar).
* Gerenciamento seguro de credenciais usando variáveis de ambiente (`.env`).

## Tecnologias Utilizadas
* **Python 3**
* **Supabase Client** (Banco de dados na nuvem)
* **Requests** (Para consumo da Z-API)
* **Python-dotenv** (Segurança de credenciais)

## Configuração da Tabela no Supabase
O script espera uma tabela chamada `Contatos` com a seguinte estrutura de colunas:
* `id` (int8, chave primária gerada automaticamente)
* `created_at` (timestamptz, gerado automaticamente)
* `nome` (text)
* `telefone` (text) -> Formato: `55849XXXXXXXX`

## Pré-requisitos e Instalação

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias executando o comando no terminal:
   ```bash
   pip install requests supabase python-dotenv


## VARIAVEIS DE AMBIENTE
* SUPABASE_URL=sua_url_do_supabase
* SUPABASE_KEY=sua_chave_anon_public
* Z_API_INSTANCE=seu_id_da_instancia_zapi
* Z_API_TOKEN=seu_token_da_zapi

## Como Executar
   python desafio.py

import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# Carregando as configurações: lendo o arquivo (.env) onde ficam as senhas
load_dotenv()

# Guardando os dados das APIs em variáveis para o código usar depois
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
Z_API_INSTANCE = os.getenv("Z_API_INSTANCE")
Z_API_TOKEN = os.getenv("Z_API_TOKEN")

def buscar_dados_no_supabase():
    """Função que conecta no Supabase e traz a lista de contatos"""
    print("[*] Conectando ao banco de dados do Supabase...")
    try:
        # Criando a conexão oficial com o link e a chave do Supabase
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Acessando a tabela 'Contatos', escolhe as colunas e puxa no máximo 3 linhas
        resposta = supabase.table("Contatos").select("nome, telefone").limit(3).execute()
        
        # Retorna os dados encontrados em formato de lista
        return resposta.data
        
    except Exception as erro:
        print(f"[-] Erro ao buscar dados no Supabase: {erro}")
        return []

def enviar_mensagem_whatsapp(nome, telefone):
    """Função que avisa a Z-API para disparar a mensagem no WhatsApp"""
    # Esse é o endereço de internet que a Z-API nos dá para enviar textos
    url_zapi = f"https://api.z-api.io/instances/{Z_API_INSTANCE}/token/{Z_API_TOKEN}/send-text"
    
    # Configurando o formato da mensagem (JSON)
    headers = {
        "Content-Type": "application/json"
    }
    
    # Criando o "pacote" com o telefone e o texto personalizado
    dados_da_mensagem = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }
    
    try:
        # O Python faz o disparo (POST) para o servidor da Z-API levando o pacote
        resposta_envio = requests.post(url_zapi, json=dados_da_mensagem, headers=headers)
        
        # Se o servidor responder 200 ou 201, significa que ele aceitou o envio!
        if resposta_envio.status_code in [200, 201]:
            print(f"[+] Mensagem enviada com sucesso para: {nome}")
        else:
            print(f"[-] Falha na Z-API para {nome}. Status Código: {resposta_envio.status_code}")
            
    except Exception as erro:
        print(f"[-] Erro de conexão ao tentar enviar para {nome}: {erro}")

def rodar_fluxo_principal():
    """O cérebro do script: junta o passo 1 com o passo 2"""
    print("=== INICIANDO SISTEMA B2BFLOW ===")
    
    # Busca a listinha de pessoas cadastradas
    lista_de_contatos = buscar_dados_no_supabase()
    
    # Se a lista estiver vazia (erro ou tabela limpa), o código para aqui
    if not lista_de_contatos:
        print("[-] Nenhum contato encontrado para processar.")
        return
        
    print(f"[+] Sucesso! Encontramos {len(lista_de_contatos)} contato(s).")
    
    # O comando 'for' faz o Python ler um contato por vez da lista
    for contato in lista_de_contatos:
        nome_da_pessoa = contato.get("nome")
        telefone_da_pessoa = contato.get("telefone")
        
        # Garante que o contato tem nome e telefone preenchidos antes de enviar
        if nome_da_pessoa and telefone_da_pessoa:
            enviar_mensagem_whatsapp(nome_da_pessoa, telefone_da_pessoa)
            
    print("=== FLUXO FINALIZADO COM SUCESSO ===")

# Indica que, ao abrir o arquivo, a execução deve começar pela função principal
if __name__ == "__main__":
    rodar_fluxo_principal()
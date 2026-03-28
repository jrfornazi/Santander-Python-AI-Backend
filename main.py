import pandas as pd
import openai
import os

# ==========================================
# CONFIGURAÇÃO DA API (OPENAI)
# ==========================================
# Dica: No seu computador, você pode definir uma variável de ambiente 
# ou colocar a chave diretamente aqui para testar (mas não suba a chave no GitHub!)
openai.api_key = "SUA_CHAVE_AQUI"

def gerar_mensagem_ia(nome, saldo):
    """
    Função que simula a etapa de TRANSFORMAÇÃO usando IA.
    Se a chave da API não for válida, ele usa um fallback (plano B).
    """
    prompt = f"Crie uma mensagem curta para o cliente {nome} sobre investimentos. Ele tem R${saldo} na conta. Seja motivador."
    
    try:
        # Chamada para a API da OpenAI (GPT-3.5)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Fallback: Caso a API dê erro ou você esteja sem crédito/chave
        return f"Olá {nome}, vimos que você tem R${saldo} disponível. Que tal conhecer nossas opções de CDB?"

# ==========================================
# ETAPA 1: EXTRAÇÃO (E)
# ==========================================
print("Iniciando Extração...")
try:
    # Lendo o arquivo CSV que você vai criar (usuarios.csv)
    df = pd.read_csv('usuarios.csv')
    print("Dados extraídos com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'usuarios.csv' não foi encontrado!")
    # Criando dados de exemplo caso o arquivo não exista para o código não travar
    data = {
        'Nome': ['Alice', 'Bruno', 'Carla'],
        'Saldo': [5000.0, 150.0, 12000.0]
    }
    df = pd.DataFrame(data)
    print("Usando dados temporários para demonstração.")

# ==========================================
# ETAPA 2: TRANSFORMAÇÃO (T)
# ==========================================
print("Iniciando Transformação com IA...")
# Aplicando a função de geração de mensagens para cada linha do DataFrame
df['Mensagem_Personalizada'] = df.apply(lambda row: gerar_mensagem_ia(row['Nome'], row['Saldo']), axis=1)
print("Transformação concluída!")

# ==========================================
# ETAPA 3: CARGA (L)
# ==========================================
print("Iniciando Carga...")
# Salvando o resultado em um novo arquivo CSV
df.to_csv('santander_marketing_ia.csv', index=False)
print("Sucesso! O arquivo 'santander_marketing_ia.csv' foi gerado.")
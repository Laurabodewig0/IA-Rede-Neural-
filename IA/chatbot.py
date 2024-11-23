from transformers import pipeline
import json

# Carregar o modelo de geração de texto
gerador = pipeline("text-generation", model="gpt2")

# Banco de dados simples para aprendizado
ARQUIVO_CONHECIMENTOS = "conhecimentos.json"

# Função para carregar o banco de dados
def carregar_conhecimentos():
    try:
        with open(ARQUIVO_CONHECIMENTOS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar novos conhecimentos
def salvar_conhecimentos(conhecimentos):
    with open(ARQUIVO_CONHECIMENTOS, "w") as f:
        json.dump(conhecimentos, f)

# Iniciar banco de dados
conhecimentos = carregar_conhecimentos()

# Função para processar a entrada do usuário
def responder(usuario_input):
    if usuario_input in conhecimentos:
        return conhecimentos[usuario_input]
    else:
        resposta = gerador(usuario_input, max_length=50, num_return_sequences=1)[0]["generated_text"]
        conhecimentos[usuario_input] = resposta
        salvar_conhecimentos(conhecimentos)
        return resposta

# Loop de interação
print("Bem-vindo à IA generativa! Para sair, digite 'sair'.")
while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("Até mais!")
        break
    resposta = responder(entrada)
    print(f"IA: {resposta}")

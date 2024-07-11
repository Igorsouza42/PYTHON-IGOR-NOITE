# Função para processar a palavra e retornar a resposta correspondente
def processar_palavra(palavra):
    if palavra == "ping":
        return "pong"
    elif palavra == "time":
        return "Botafogo"
    elif palavra == "vivo":
        return "morto"
    else:
        return "Palavra desconhecida"

# Recebendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Processando a palavra e exibindo a resposta
resposta = processar_palavra(palavra)
print(resposta)

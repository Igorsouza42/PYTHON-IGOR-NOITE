from utils import dobro
 
# Entrada do usuario
limite_atual = float(input("Digite o limite atual do seu cartão de credito: R$"))

# Calcula o novo limite
novo_limite = dobro(limite_atual)

# Imprime os resultados
print(f"Seu limite atual é R${limite_atual:.2f}. Seu novo limite seria R${novo_limite:.2f}.")
from utils import dobro
 
# Entrada do usuario
salario_mensal = float(input("Digite o seu salario mensal: R$"))

# Calcula o novo limite
valor_recebido = dobro(salario_mensal)

# Imprime os resultados
print(f"Seu limite atual é R${salario_mensal:.2f}. Seu novo limite seria R${valor_recebido:.2f}. Como 13º salário.")


from utils import dobro
 
# Entrada do usuario
valor_emprestado = float(input("Digite o valor que deseja emprestar: R$"))

# Calcula o novo limite
total_pagar = dobro(valor_emprestado)

# Imprime os resultados
print(f"Seu limite atual é R${valor_emprestado:.2f}. Total a pagar após um ano: R${total_pagar:.2f}..")

soma = 0 # Inicializa a soma dos numeros
continuar = True # Variavel de contraste para o loop

while continuar:
    print("\nMenu:")
    print("1 - Adicionar um numero a soma")
    print("2 - Exibir soma atual")
    print("3 - sair")
    opcao = input("Escolha uma opção (1, 2 ou 3):") # Recebe a opção do usu:

    if opcao == "1":
        numero = input("Digite um número para adicionar á soma:")
        soma +- float(numero) # Adiciona o número á soma total
        print(f"Número {numero} adicionando á soma.")

    elif opcao == "2":
        print(f"Soma total: {soma}") # Exibe a soma atual
    elif opcao == "3":
        break 
    else:
     print("Opção ínvalida, Por favor, escolha 1, 2 ou 3.") # Mensagem para opção inválida

    print("Programa encerrado. Soma final:", soma) # Exibe a soma final quando o loop termina


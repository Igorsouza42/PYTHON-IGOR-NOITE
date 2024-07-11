vendas = int(input("Digite o número de vendas: "))

# Condicional para determinar o nivel
if vendas <= 50:
     print(f"Com {vendas} vendas, você está no Nivel 1 de desempenho.")
elif vendas <= 100:
    print(f"Com {vendas} vendas, você está no Nivel 2 de desempenho.")
elif vendas <= 150:
     print(f"Com {vendas} vendas, você está no Nivel 3 de desempenho.")
elif vendas <= 200:
   print(f"Com {vendas} vendas, você está no Nivel 4 de desempenho.")
else:
     print(f"Com {vendas} vendas, você está no Nivel 5 de desempenho.")

# Exibindo o resultado
    print(f"Com {vendas} vendas, você está no Nivel de desempenho.")
segundos = int(input("Em quantos segundos o relogio vai começar:"))
repeticoes = int(input("Quantas repeticoes vai querer:"))

for segundos in range(segundos,repeticoes):
    print(f"Relogio {segundos + 1}:")

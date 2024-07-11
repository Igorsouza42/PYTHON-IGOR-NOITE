somatorio = 0
x = int(input("Digite 1 caso queira somar um número e O caso ver o somatorio final:"))
while x == 1:
    numero = int(input("Digite o numero que gostaria de somar:"))
    x = int(input("Digite 1 caso queira somar um número e O caso ver o somatorio final:"))
    somatorio = somatorio + numero

print(somatorio)

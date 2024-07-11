idade = int(input("Digite sua idade:"))
if idade < 16:
    print("Voce não está elegivel para votar.")
elif 18 <= idade < 70:
    print("Seu voto é obrigatório.")
else:
    print("Voce está elegivel para votar, mas não é obrigatorio")
 

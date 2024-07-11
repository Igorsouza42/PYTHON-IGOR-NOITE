cartãoblack= input("Você tem acesso ao cartão black para usar a sala vip? (sim/não): ").lower()
ingresso = input("Você comprou ou tem ingresso a sala vip: (sim/não): ").lower()
               
if cartãoblack == "sim" and ingresso == "sim":
    print("Você tem acesso a sala vip!")
else: 
    print("Você não tem acesso a sala vip.")


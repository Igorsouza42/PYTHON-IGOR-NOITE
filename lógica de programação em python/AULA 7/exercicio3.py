# Perguntando a hora ao úsuario
hora_atual = int(input("Digite a hora atual (formato 24h, apenas a hora):"))

# Verificando se está fora do horário de expediente
if hora_atual < 8 or hora_atual >= 18:
 print("Erro: Fora do expediente. O sistema só funciona entre 8h até 17:")
else: 

# Se estiver dentro do horário de expediente, processeguir com a agenda
  for hora in range(hora_atual, hora_atual + 8):
   atividade = input(f"O que voce está fazendo ás {hora}h?")    
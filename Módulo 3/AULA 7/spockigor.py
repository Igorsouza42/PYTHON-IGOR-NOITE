import random

# Função que determina o vencedor
def determinar_vencedor(jogador1, jogador2):
    vitorias = {
        "pedra": ["tesoura", "lagarto"],
        "papel": ["pedra", "spock"],
        "tesoura": ["papel", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    
    if jogador1 == jogador2:
        return "Empate"
    elif jogador2 in vitorias[jogador1]:
        return "Jogador 1 vence"
    else:
        return "Jogador 2 vence"

# Função que recebe a escolha do jogador
def obter_escolha_jogador(jogador):
    escolha = input(f"{jogador}, escolha entre pedra, papel, tesoura, lagarto, spock: ").lower()
    while escolha not in ["pedra", "papel", "tesoura", "lagarto", "spock"]:
        print("Escolha inválida, tente novamente.")
        escolha = input(f"{jogador}, escolha entre pedra, papel, tesoura, lagarto, spock: ").lower()
    return escolha

# Função principal do jogo
def jogar():
    modo = input("Escolha o modo de jogo: pvp ou pvm: ").lower()
    
    if modo == "pvp":
        jogador1_escolha = obter_escolha_jogador("Jogador 1")
        jogador2_escolha = obter_escolha_jogador("Jogador 2")
    elif modo == "pvm":
        jogador1_escolha = obter_escolha_jogador("Jogador")
        jogador2_escolha = random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])
        print(f"Máquina escolheu: {jogador2_escolha}")
    else:
        print("Modo de jogo inválido, escolha PvP ou PvM.")
        return
    
    resultado = determinar_vencedor(jogador1_escolha, jogador2_escolha)
    print(resultado)

# Executar o jogo
if __name__ == "__main__":
    jogar()

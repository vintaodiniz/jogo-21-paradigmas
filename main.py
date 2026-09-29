# Jogo 21 (Blackjack) - Paradigma Imperativo
# Desenvolvido para a disciplina de Paradigmas de Programação - UNAMA

def exibir_regras():
    print("\n================ REGRAS DO JOGO 21 ================")
    print("1. O objetivo é alcançar ou chegar o mais perto possível de 21 pontos.")
    print("2. Cartas numéricas valem o próprio valor, e figuras (J, Q, K) valem 10.")
    print("3. Se a pontuação ultrapassar 21, você estoura e perde automaticamente.")
    print("====================================================")

def iniciar_partida():
    print("\n--- PARTIDA INICIADA ---")
    print("Lógica do jogo em desenvolvimento pelo Integrante 1...")

def main():
    continuar = True
    while continuar:
        print("\n====================")
        print("    JOGO 21 - UNAMA")
        print("====================")
        print("1. Iniciar Partida")
        print("2. Ver Regras")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            iniciar_partida()
        elif opcao == "2":
            exibir_regras()
        elif opcao == "3":
            print("Saindo do jogo. Até mais!")
            continuar = False
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
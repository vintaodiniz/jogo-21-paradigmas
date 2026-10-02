

def exibir_regras():
    print("\n========================================")
    print("          REGRAS DO JOGO 21 (BLACKJACK)   ")
    print("========================================")
    print("1. O objetivo é chegar a 21 pontos ou perto, sem passar.")
    print("2. Cartas de 2 a 10 valem o próprio valor.")
    print("3. J, Q e K valem 10 pontos.")
    print("4. Quem passar de 21 pontos estoura e perde a rodada.")
    print("========================================")
    input("\nPressione ENTER para voltar ao menu...")

def main():
    continuar = True
    while continuar:
        print("\n========================================")
        print("            JOGO 21 - UNAMA             ")
        print("========================================")
        print("1. Iniciar Partida")
        print("2. Ver Regras")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            print("\n[Aviso] O modo de jogo será iniciado em breve!")
        elif opcao == "2":
            exibir_regras()
        elif opcao == "3":
            print("\nA sair do jogo. Até breve!")
            continuar = False
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
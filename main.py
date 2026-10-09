from logica import jogar_rodada
from economia import inicializar_banca, gerenciar_aposta, atualizar_saldo, verificar_fim_jogo


def iniciar_partida():
    """Executa a partida completa: várias rodadas com saldo e apostas."""
    saldo = inicializar_banca()
    rodada = 1
    print(f"\n🎰 Partida iniciada! Seu saldo inicial: R$ {saldo}")
    print("Meta: alcançar R$ 50.000 para falir o dono do jogo!")

    while True:
        # Verificar se o jogo acabou (saldo zerado ou meta atingida)
        status = verificar_fim_jogo(saldo)
        if status != "continuar":
            break

        print(f"\n--- RODADA {rodada} ---")
        rodada = rodada + 1

        # Solicitar aposta ao jogador
        aposta = gerenciar_aposta(saldo)
        if aposta == 0:
            break

        # Jogar a rodada de cartas (logica.py)
        resultado = jogar_rodada()

        # Atualizar o saldo com base no resultado (economia.py)
        saldo = atualizar_saldo(saldo, aposta, resultado)
        print(f"\n💰 Saldo atual: R$ {saldo}")

    print("\nVoltando ao menu principal...")
    input("Pressione ENTER para continuar...")


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
            iniciar_partida()
        elif opcao == "2":
            exibir_regras()
        elif opcao == "3":
            print("\nA sair do jogo. Até breve!")
            continuar = False
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
# Ficheiro: logica.py
# Integrante 1 (Thiago): Sistema de Cartas e Regras do Jogo 21

import random


def sortear_carta():
    """Retorna uma carta aleatória do baralho.
    Cartas possíveis: 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'.
    """
    cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    return random.choice(cartas)


def valor_da_carta(carta):
    """Retorna o valor numérico de uma carta.
    Figuras (J, Q, K) valem 10. Ás vale 11 inicialmente (ajustado depois).
    """
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11
    return carta


def calcular_pontos(mao):
    """Soma os pontos da mão, ajustando Áses de 11 para 1 se ultrapassar 21."""
    pontos = 0
    quantidade_ases = 0

    # Somar cada carta da mão
    for carta in mao:
        pontos = pontos + valor_da_carta(carta)
        if carta == 'A':
            quantidade_ases = quantidade_ases + 1

    # Se estourou e tem Ás contando como 11, reduz para 1 (tira 10)
    while pontos > 21 and quantidade_ases > 0:
        pontos = pontos - 10
        quantidade_ases = quantidade_ases - 1

    return pontos


def exibir_mao(nome, mao, esconder_segunda=False):
    """Exibe as cartas e a pontuação de um participante.
    Se esconder_segunda=True, oculta a segunda carta (usado para a banca).
    """
    if esconder_segunda and len(mao) >= 2:
        print(f"  {nome}: [{mao[0]}, ?] (Pontuação oculta)")
    else:
        pontos = calcular_pontos(mao)
        print(f"  {nome}: {mao} -> {pontos} pontos")


def jogar_rodada():
    """Executa uma rodada completa do Jogo 21.
    Retorna 'vitoria', 'derrota' ou 'empate' do ponto de vista do jogador,
    compatível com a função atualizar_saldo do módulo economia.
    """
    # Distribuir 2 cartas iniciais para cada um
    mao_jogador = [sortear_carta(), sortear_carta()]
    mao_banca = [sortear_carta(), sortear_carta()]

    print("\n========================================")
    print("         INÍCIO DA RODADA")
    print("========================================")
    exibir_mao("Banca  ", mao_banca, esconder_segunda=True)
    exibir_mao("Jogador", mao_jogador)

    # Verificar Blackjack imediato (21 pontos com 2 cartas)
    if calcular_pontos(mao_jogador) == 21:
        print("\n🔥 BLACKJACK! Você fez 21 pontos de cara!")
        exibir_mao("Banca  ", mao_banca)
        if calcular_pontos(mao_banca) == 21:
            print("A banca também tem 21! Empate!")
            return "empate"
        return "vitoria"

    # ---- Turno do Jogador ----
    while True:
        opcao = input("\nDeseja comprar mais uma carta? (s/n): ").strip().lower()

        if opcao == 's':
            nova_carta = sortear_carta()
            mao_jogador.append(nova_carta)
            print(f"  Você comprou: {nova_carta}")
            exibir_mao("Jogador", mao_jogador)

            pontos_jogador = calcular_pontos(mao_jogador)
            if pontos_jogador > 21:
                print("\n💥 Estourou! Passou de 21 pontos. Derrota na rodada.")
                return "derrota"
            elif pontos_jogador == 21:
                print("  Você atingiu 21 pontos exatos!")
                break
        elif opcao == 'n':
            break
        else:
            print("  Opção inválida! Digite 's' para sim ou 'n' para não.")

    pontos_jogador = calcular_pontos(mao_jogador)

    # ---- Turno da Banca (Máquina) ----
    print("\n----------------------------------------")
    print("         TURNO DA BANCA")
    print("----------------------------------------")
    exibir_mao("Banca  ", mao_banca)

    # A banca compra cartas enquanto tiver menos de 17 pontos
    while calcular_pontos(mao_banca) < 17:
        nova_carta = sortear_carta()
        mao_banca.append(nova_carta)
        print(f"  A banca comprou: {nova_carta}")
        exibir_mao("Banca  ", mao_banca)

    pontos_banca = calcular_pontos(mao_banca)

    # ---- Resultado da Rodada ----
    print("\n========================================")
    print("         RESULTADO DA RODADA")
    print("========================================")
    print(f"  Jogador: {pontos_jogador} pontos | Banca: {pontos_banca} pontos")

    if pontos_banca > 21:
        print("  🎉 A banca estourou! Você venceu!")
        return "vitoria"
    elif pontos_jogador > pontos_banca:
        print("  🎉 Você fez mais pontos! Vitória!")
        return "vitoria"
    elif pontos_jogador < pontos_banca:
        print("  ❌ A banca fez mais pontos. Derrota!")
        return "derrota"
    else:
        print("  🤝 Mesma pontuação. Empate!")
        return "empate"

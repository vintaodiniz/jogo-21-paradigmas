"""Saldo, apostas e condições de encerramento do Jogo 21."""

SALDO_INICIAL = 1000
META_VITORIA = 50000


def inicializar_banca():
    """Começa cada nova partida com o mesmo saldo."""
    return SALDO_INICIAL


def gerenciar_aposta(saldo_atual):
    """Solicita uma aposta inteira válida; retorna zero se não houver saldo."""
    if saldo_atual <= 0:
        print("Não há saldo disponível para apostar.")
        return 0

    print(f"\nSeu saldo atual: R$ {saldo_atual}")
    while True:
        try:
            aposta = int(input("Quanto deseja apostar nesta rodada? R$ "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        if aposta <= 0:
            print("A aposta deve ser maior que zero.")
        elif aposta > saldo_atual:
            print("Não tem saldo suficiente para essa aposta!")
        else:
            return aposta


def atualizar_saldo(saldo_atual, aposta, resultado):
    """Liquida uma rodada sem desconto antecipado da aposta.

    resultado: 'vitoria', 'derrota' ou 'empate', do ponto de vista do jogador.
    Vitória soma a aposta, derrota subtrai e empate mantém o saldo.
    """
    if type(saldo_atual) is not int or saldo_atual < 0:
        raise ValueError("O saldo deve ser um número inteiro não negativo.")
    if type(aposta) is not int or aposta <= 0 or aposta > saldo_atual:
        raise ValueError("A aposta deve ser inteira, positiva e não superar o saldo.")

    if resultado == "vitoria":
        saldo_atual = saldo_atual + aposta
    elif resultado == "derrota":
        saldo_atual = saldo_atual - aposta
    elif resultado != "empate":
        raise ValueError("Resultado inválido: use vitoria, derrota ou empate.")

    return saldo_atual


def verificar_fim_jogo(saldo):
    """Informa se a partida terminou por atingir a meta ou perder a banca."""
    if saldo >= META_VITORIA:
        print("\nPARABÉNS! Você faliu o dono do jogo!")
        return "vitoria"
    elif saldo <= 0:
        print("\nSUA BANCA ESTOUROU!")
        return "derrota"

    return "continuar"

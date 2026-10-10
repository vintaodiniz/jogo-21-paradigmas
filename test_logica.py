"""Execute com: python -m unittest -v test_logica"""

import unittest
from unittest.mock import patch

import logica


class TestLogica(unittest.TestCase):
    def test_sortear_carta_retorna_carta_valida(self):
        cartas_validas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        for _ in range(50):
            carta = logica.sortear_carta()
            self.assertIn(carta, cartas_validas)

    def test_valor_da_carta(self):
        # Figuras valem 10
        self.assertEqual(logica.valor_da_carta('J'), 10)
        self.assertEqual(logica.valor_da_carta('Q'), 10)
        self.assertEqual(logica.valor_da_carta('K'), 10)
        # Ás vale 11 inicialmente
        self.assertEqual(logica.valor_da_carta('A'), 11)
        # Numéricas mantêm o valor
        for num in range(2, 11):
            self.assertEqual(logica.valor_da_carta(num), num)

    def test_calcular_pontos_sem_as(self):
        self.assertEqual(logica.calcular_pontos([2, 5, 8]), 15)
        self.assertEqual(logica.calcular_pontos([10, 'K']), 20)
        self.assertEqual(logica.calcular_pontos(['J', 'Q', 5]), 25)

    def test_calcular_pontos_com_as_blackjack(self):
        # Ás + 10 ou figura vale 21
        self.assertEqual(logica.calcular_pontos(['A', 10]), 21)
        self.assertEqual(logica.calcular_pontos(['A', 'K']), 21)

    def test_calcular_pontos_ajuste_dinamico_do_as(self):
        # Ás começa valendo 11, mas ajusta para 1 se estourar 21
        self.assertEqual(logica.calcular_pontos(['A', 10, 5]), 16)
        self.assertEqual(logica.calcular_pontos(['A', 9]), 20)
        # Múltiplos ases
        self.assertEqual(logica.calcular_pontos(['A', 'A']), 12)  # 11 + 1
        self.assertEqual(logica.calcular_pontos(['A', 'A', 10]), 12)  # 1 + 1 + 10
        self.assertEqual(logica.calcular_pontos(['A', 'A', 'A']), 13)  # 11 + 1 + 1

    @patch("builtins.print")
    def test_jogar_rodada_blackjack_jogador(self, _print):
        # Mock do baralho: jogador ganha [A, 10], banca ganha [10, 7]
        with patch("logica.sortear_carta", side_effect=['A', 10, 10, 7]):
            resultado = logica.jogar_rodada()
            self.assertEqual(resultado, "vitoria")

    @patch("builtins.print")
    def test_jogar_rodada_estouro_jogador(self, _print):
        # Jogador tira [10, 6], pede mais uma carta [10] e estoura (>21)
        with patch("logica.sortear_carta", side_effect=[10, 6, 10, 7, 10]):
            with patch("builtins.input", side_effect=['s']):
                resultado = logica.jogar_rodada()
                self.assertEqual(resultado, "derrota")

    @patch("builtins.print")
    def test_jogar_rodada_jogador_para_e_vence_banca(self, _print):
        # Jogador [10, 9] (19 pts), para ('n'). Banca [10, 7] (17 pts, para).
        with patch("logica.sortear_carta", side_effect=[10, 9, 10, 7]):
            with patch("builtins.input", side_effect=['n']):
                resultado = logica.jogar_rodada()
                self.assertEqual(resultado, "vitoria")


if __name__ == "__main__":
    unittest.main()

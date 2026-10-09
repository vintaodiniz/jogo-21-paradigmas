"""Execute com: python -m unittest -v test_economia"""

import unittest
from unittest.mock import patch

import economia


class TestEconomia(unittest.TestCase):
    def test_nova_partida_reinicia_banca(self):
        saldo = economia.inicializar_banca()
        saldo = economia.atualizar_saldo(saldo, 100, "derrota")
        self.assertEqual(saldo, 900)
        self.assertEqual(economia.inicializar_banca(), 1000)

    @patch("builtins.print")
    def test_repete_entrada_ate_aposta_valida(self, _print):
        with patch("builtins.input", side_effect=["abc", "", "1.5", "0", "-10", "1001", "100"]) as entrada:
            self.assertEqual(economia.gerenciar_aposta(1000), 100)
            self.assertEqual(entrada.call_count, 7)

    @patch("builtins.print")
    def test_permite_apostar_toda_banca(self, _print):
        with patch("builtins.input", return_value="1000"):
            self.assertEqual(economia.gerenciar_aposta(1000), 1000)

    @patch("builtins.print")
    def test_sem_saldo_nao_solicita_aposta(self, _print):
        with patch("builtins.input") as entrada:
            self.assertEqual(economia.gerenciar_aposta(0), 0)
            entrada.assert_not_called()

    def test_resultados_da_rodada(self):
        for resultado, esperado in [("vitoria", 1100), ("derrota", 900), ("empate", 1000)]:
            with self.subTest(resultado=resultado):
                self.assertEqual(economia.atualizar_saldo(1000, 100, resultado), esperado)

    def test_rejeita_liquidacao_invalida(self):
        for saldo, aposta, resultado in [
            (1000, 0, "vitoria"), (1000, -1, "derrota"),
            (1000, 1001, "derrota"), (1000, 1.5, "vitoria"),
            (1000, True, "vitoria"), (-1, 1, "derrota"),
            (1000.5, 100, "vitoria"), (1000, 100, "desconhecido"),
        ]:
            with self.subTest(saldo=saldo, aposta=aposta, resultado=resultado):
                with self.assertRaises(ValueError):
                    economia.atualizar_saldo(saldo, aposta, resultado)

    @patch("builtins.print")
    def test_limites_de_encerramento(self, _print):
        for saldo, esperado in [(-1, "derrota"), (0, "derrota"), (1, "continuar"),
                                (49999, "continuar"), (50000, "vitoria"), (51000, "vitoria")]:
            with self.subTest(saldo=saldo):
                self.assertEqual(economia.verificar_fim_jogo(saldo), esperado)

    @patch("builtins.print")
    def test_rodadas_ate_meta_e_falencia(self, _print):
        saldo = economia.atualizar_saldo(49000, 1000, "vitoria")
        self.assertEqual(economia.verificar_fim_jogo(saldo), "vitoria")
        saldo = economia.atualizar_saldo(1000, 1000, "derrota")
        self.assertEqual(economia.verificar_fim_jogo(saldo), "derrota")


if __name__ == "__main__":
    unittest.main()

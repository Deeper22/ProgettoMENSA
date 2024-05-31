import unittest
from unittest.mock import patch
from main import Utente
from io import StringIO

class TestUtente(unittest.TestCase):

    @patch('builtins.input', side_effect=['Mario'])
    def test_controllo_stringa_valida(self, mock_input):
        utente = Utente()
        self.assertEqual(utente.controllo_Stringa('Mario'), 'Mario')

    @patch('builtins.input', side_effect=['', 'Mario'])
    def test_controllo_stringa_non_valida(self, mock_input):
        utente = Utente()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.assertEqual(utente.controllo_Stringa(''), 'Mario')
            self.assertIn('Errore! Inserire stringa non vuota', fake_output.getvalue())

    @patch('builtins.input', side_effect=['1234567'])
    def test_controllo_matricola_valida(self, mock_input):
        utente = Utente()
        self.assertEqual(utente.controllo_Matricola('1234567'), '1234567')

    @patch('builtins.input', side_effect=['123', '1234567'])
    def test_controllo_matricola_non_valida(self, mock_input):
        utente = Utente()

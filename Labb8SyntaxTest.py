
import unittest
from main import read_molekyl
from linkedQfile import LinkedQ, Syntaxfel


class TestMolekylSyntax(unittest.TestCase):
    def test_korrekt_molekyl(self):
        korrekta_molekyler = ["H2", "P21", "Ag3", "Fe12", "Xx5", "H10100"]
        for molekyl in korrekta_molekyler:
            queue = LinkedQ()
            for char in molekyl:
                queue.enqueue(char)
            try:
                read_molekyl(queue)
            except Syntaxfel:
                self.fail(f"Korrekt molekyl misslyckades: {molekyl}")

    def test_fel_molekyl(self):
        fel_molekyler = {
            "a": "Saknad stor bokstav vid radslutet a",
            "cr12": "Saknad stor bokstav vid radslutet cr12",
            "8": "Saknad stor bokstav vid radslutet 8",
            "Cr0": "För litet tal vid radslutet ",
            "Pb1": "För litet tal vid radslutet",
            "H01011": "För litet tal vid radslutet 1011",
            "K01": "För litet tal vid radslutet 1"
        }
        for molekyl, expected_message in fel_molekyler.items():
            queue = LinkedQ()
            for char in molekyl:
                queue.enqueue(char)
            with self.assertRaises(Syntaxfel) as cm:
                read_molekyl(queue)
            self.assertEqual(str(cm.exception), expected_message)


unittest.main(argv=[''], verbosity=2, exit=False)

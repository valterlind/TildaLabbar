import unittest
from Labb9 import MoleculeParser


class Syntaxtest(unittest.TestCase):
    def test_one_a(self):
        output = MoleculeParser("C(Xx4)5").parse_to_output()
        expected = "Okänd atom vid radslutet 4)5"
        print(f"Test input: C(Xx4)5\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_b(self):
        output = MoleculeParser("C(OH4)C").parse_to_output()
        expected = "Saknad siffra vid radslutet C"
        print(f"Test input: C(OH4)C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_c(self):
        output = MoleculeParser("C(OH4C").parse_to_output()
        expected = "Saknad högerparentes vid radslutet "
        print(f"Test input: C(OH4C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_d(self):
        output = MoleculeParser("H2O)Fe").parse_to_output()
        expected = "Felaktig gruppstart vid radslutet )Fe"
        print(f"Test input: H2O)Fe\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_e(self):
        output = MoleculeParser("H0").parse_to_output()
        expected = "För litet tal vid radslutet "
        print(f"Test input: H0\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_f(self):
        output = MoleculeParser("H1C").parse_to_output()
        expected = "För litet tal vid radslutet C"
        print(f"Test input: H1C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_g(self):
        output = MoleculeParser("H02C").parse_to_output()
        expected = "För litet tal vid radslutet 2C"
        print(f"Test input: H02C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_h(self):
        output = MoleculeParser("Nacl").parse_to_output()
        expected = "Saknad stor bokstav vid radslutet cl"
        print(f"Test input: Nacl\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_i(self):
        output = MoleculeParser("a").parse_to_output()
        expected = "Saknad stor bokstav vid radslutet a"
        print(f"Test input: a\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_j(self):
        output = MoleculeParser("(Cl)2)3").parse_to_output()
        expected = "Felaktig gruppstart vid radslutet )3"
        print(f"Test input: (Cl)2)3\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_k(self):
        output = MoleculeParser(")").parse_to_output()
        expected = "Felaktig gruppstart vid radslutet )"
        print(f"Test input: )\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_l(self):
        output = MoleculeParser("2").parse_to_output()
        expected = "Felaktig gruppstart vid radslutet 2"
        print(f"Test input: 2\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_m(self):
        output = MoleculeParser("Na").parse_to_output()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Na\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_n(self):
        output = MoleculeParser("H2O").parse_to_output()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: H2O\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_o(self):
        output = MoleculeParser("Si(C3(COOH)2)4(H2O)7").parse_to_output()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Si(C3(COOH)2)4(H2O)7\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_p(self):
        output = MoleculeParser("Na332").parse_to_output()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Na332\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()

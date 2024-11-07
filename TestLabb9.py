import unittest
import main2 as s  # Importerar main2 och förväntar sig att testOutput finns


class Syntaxtest(unittest.TestCase):
    def test_one_a(self):
        output = s.testOutput("C(Xx4)5").strip()
        expected = "Okänd atom vid radslutet 4)5"
        print(f"Test input: C(Xx4)5\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_b(self):
        output = s.testOutput("C(OH4)C").strip()
        expected = "Saknad siffra vid radslutet C"
        print(f"Test input: C(OH4)C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_c(self):
        output = s.testOutput("C(OH4C").strip()
        expected = "Saknad högerparentes vid radslutet "
        print(f"Test input: C(OH4C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_d(self):
        output = s.testOutput("H2O)Fe").strip()
        expected = "Felaktig gruppstart vid radslutet )Fe"
        print(f"Test input: H2O)Fe\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_e(self):
        output = s.testOutput("H0").strip()
        expected = "För litet tal vid radslutet "
        print(f"Test input: H0\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_f(self):
        output = s.testOutput("H1C").strip()
        expected = "För litet tal vid radslutet C"
        print(f"Test input: H1C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_g(self):
        output = s.testOutput("H02C").strip()
        expected = "För litet tal vid radslutet 2C"
        print(f"Test input: H02C\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_h(self):
        output = s.testOutput("Nacl").strip()
        expected = "Saknad stor bokstav vid radslutet cl"
        print(f"Test input: Nacl\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_i(self):
        output = s.testOutput("a").strip()
        expected = "Saknad stor bokstav vid radslutet a"
        print(f"Test input: a\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_j(self):
        output = s.testOutput("(Cl)2)3").strip()
        expected = "Felaktig gruppstart vid radslutet )3"
        print(f"Test input: (Cl)2)3\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_k(self):
        output = s.testOutput(")").strip()
        expected = "Felaktig gruppstart vid radslutet )"
        print(f"Test input: )\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_l(self):
        output = s.testOutput("2").strip()
        expected = "Felaktig gruppstart vid radslutet 2"
        print(f"Test input: 2\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_m(self):
        output = s.testOutput("Na").strip()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Na\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_n(self):
        output = s.testOutput("H2O").strip()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: H2O\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_o(self):
        output = s.testOutput("Si(C3(COOH)2)4(H2O)7").strip()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Si(C3(COOH)2)4(H2O)7\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)

    def test_one_p(self):
        output = s.testOutput("Na332").strip()
        expected = "Formeln är syntaktiskt korrekt"
        print(f"Test input: Na332\nExpected: '{expected}'\nActual:   '{output}'\n")
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()

# Testar syntaxen
class TestMolekylSyntax(unittest.TestCase):
    def test_korrekt_molekyl(self):
        try:
            kontrollera_molekyl("H2")
            kontrollera_molekyl("O2")
            kontrollera_molekyl("He")
            self.assertTrue(True)  # Om vi inte får något undantag är det korrekt
        except Syntaxfel:
            self.fail("Fick oväntat Syntaxfel för korrekt molekyl")

    def test_fel_molekyl(self):
        with self.assertRaises(Syntaxfel) as cm:
            kontrollera_molekyl("h2")
        self.assertEqual(str(cm.exception), "Saknad stor bokstav vid radslutet: h2")

        with self.assertRaises(Syntaxfel) as cm:
            kontrollera_molekyl("H1")
        self.assertEqual(str(cm.exception), "För litet tal vid radslutet: 1")


#unittest.main()

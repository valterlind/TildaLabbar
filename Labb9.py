import sys
from linkedQfile import LinkedQ, Syntaxfel  # Importera LinkedQ och Syntaxfel från linkedQfile

# Lista över giltiga atomer
valid_atoms = {"H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
               "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br",
               "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te",
               "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm",
               "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
               "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
               "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"}


class MoleculeParser:
    def __init__(self, formula):
        self.queue = LinkedQ()
        for char in formula:
            self.queue.enqueue(char)

    def readformula(self):
        try:
            # Kontrollera om formeln börjar med ")" eller en siffra
            first_char = self.current_char()
            if first_char == ")":
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")
            if first_char.isdigit():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")
            
            # Starta analysen med readmol()
            self.readmol()
            
            # Om kön inte är tom efter analysen, så finns ett syntaxfel
            if not self.queue.isEmpty():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")
            
            print("Formeln är syntaktiskt korrekt")
        
        except Syntaxfel as e:
            print(e)

    def readmol(self):
        """<mol> ::= <group> | <group><mol>"""
        self.readgroup()
        while not self.queue.isEmpty() and self.queue.peek() != ')':
            self.readgroup()

    def readgroup(self):
        """<group> ::= <atom> | <atom><num> | (<mol>) <num>"""
        if self.current_char() == '(':
            self.queue.dequeue()
            self.readmol()
            if self.current_char() != ')':
                raise Syntaxfel(f"Saknad högerparentes vid radslutet {self.remaining_formula()}")
            self.queue.dequeue()
            self.readnum()
        else:
            self.readatom()
            if self.current_char() and self.current_char().isdigit():
                self.readnum()

    def readatom(self):
        """<atom> ::= <LETTER> | <LETTER><letter>"""
        letter = self.readletter()
        atom = letter
        if self.current_char() and self.current_char().islower():
            atom += self.queue.dequeue()
        if atom not in valid_atoms:
            raise Syntaxfel(f"Okänd atom vid radslutet {self.remaining_formula()}")

    def readletter(self):
        """<LETTER>::= A | B | C | ... | Z"""
        if self.current_char() and self.current_char().isupper():
            return self.queue.dequeue()
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {self.remaining_formula()}")

    def readnum(self):
        """<num> ::= 2 | 3 | 4 | ..."""
        num = ''
        # Spara siffror i num
        while self.current_char() and self.current_char().isdigit():
            num += self.current_char()  # Samla siffror
            self.queue.dequeue()  # Fortsätt i kön

        # Kontrollera om num är tomt
        if num == "":
            raise Syntaxfel("Saknad siffra vid radslutet " + self.remaining_formula())

        # Om talet börjar med "0" men inte är exakt "0", så ge fel
        if num.startswith("0") and num != "0":
            raise Syntaxfel("För litet tal vid radslutet " + num.lstrip("0") + self.remaining_formula())
        elif num.startswith("1") and int(num) < 2:
            raise Syntaxfel("För litet tal vid radslutet " + num.lstrip("1") + self.remaining_formula())

        if int(num) == 0:
            raise Syntaxfel("För litet tal vid radslutet" + self.remaining_formula())

        # Om num är mindre än 2, ge fel och inkludera num och den återstående formeln
        if int(num) < 2:
            raise Syntaxfel("För litet tal vid radslutet " + num + self.remaining_formula())

    def current_char(self):
        """Returns the current character or None if queue is empty."""
        return self.queue.peek()

    def remaining_formula(self):
        """Returns the remaining formula in the queue as a string without emptying it."""
        temp_queue = LinkedQ()  # Skapa en temporär kö
        remaining = []

        while not self.queue.isEmpty():
            char = self.queue.dequeue()
            remaining.append(char)
            temp_queue.enqueue(char)  # Lagra tillfälligt för att återskapa kön

        # Återställ kön efter att vi läst av alla kvarvarande element
        self.queue = temp_queue
        return ''.join(remaining)

  
    def parse_to_output(self):
        """Parsar och returnerar en sträng som visar resultatet, utan att skriva ut."""
        try:
            self.readformula()
            if not self.queue.isEmpty():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")
            return "Formeln är syntaktiskt korrekt"
        except Syntaxfel as e:
            return str(e)


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        parser = MoleculeParser(line)
        parser.readformula()


if __name__ == "__main__":
    main()

def testOutput(formula):
    """Används för att testa utmatning från MoleculeParser."""
    parser = MoleculeParser(formula)
    return parser.parse_to_output()


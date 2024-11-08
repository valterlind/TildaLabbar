import sys
from linkedQfile import LinkedQ, Syntaxfel


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
        self.position = 0  # Track the position in the formula
        for char in formula:
            self.queue.enqueue(char)

    def readformula(self):
        try:
            first_char = self.current_char()
            if first_char == ")" or first_char.isdigit():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")

            self.readmol()

            if not self.queue.isEmpty():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")

            return "Formeln är syntaktiskt korrekt"

        except Syntaxfel as e:
            return str(e)

    def readmol(self):
        self.readgroup()
        while not self.queue.isEmpty() and self.queue.peek() != ')':
            self.readgroup()

    def readgroup(self):
        if self.current_char() == '(':
            self.queue.dequeue()
            self.position += 1
            self.readmol()
            if self.current_char() != ')':
                raise Syntaxfel(f"Saknad högerparentes vid radslutet {self.remaining_formula()}")
            self.queue.dequeue()
            self.position += 1
            self.readnum()
        else:
            self.readatom()
            if self.current_char() and self.current_char().isdigit():
                self.readnum()

    def readatom(self):
        letter = self.readletter()
        atom = letter
        if self.current_char() and self.current_char().islower():
            atom += self.queue.dequeue()
            self.position += 1
        if atom not in valid_atoms:
            raise Syntaxfel(f"Okänd atom vid radslutet {self.remaining_formula()}")

    def readletter(self):
        if self.current_char() and self.current_char().isupper():
            self.position += 1
            return self.queue.dequeue()
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {self.remaining_formula()}")

    def readnum(self):
        num = ''
        while self.current_char() and self.current_char().isdigit():
            num += self.current_char()
            self.queue.dequeue()
            self.position += 1

        if num == "":
            raise Syntaxfel("Saknad siffra vid radslutet " + self.remaining_formula())

        if num == "0" or num == "1":
            raise Syntaxfel("För litet tal vid radslutet " + self.remaining_formula())
        elif num.startswith("0"):
            remaining_part = num.lstrip("0") + self.remaining_formula()
            raise Syntaxfel("För litet tal vid radslutet " + remaining_part)
        elif int(num) < 2:
            raise Syntaxfel("För litet tal vid radslutet " + num + self.remaining_formula())

    def current_char(self):
        return self.queue.peek()

    def remaining_formula(self):
        temp_queue = LinkedQ()
        remaining = []
        while not self.queue.isEmpty():
            char = self.queue.dequeue()
            remaining.append(char)
            temp_queue.enqueue(char)
        self.queue = temp_queue
        return ''.join(remaining)

    def parse_to_output(self):
        return self.readformula()


def testOutput(formula):
    parser = MoleculeParser(formula)
    return parser.parse_to_output()


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '#':  # Terminate if line is '#'
            break
        parser = MoleculeParser(line)
        output = parser.parse_to_output()
        print(output)


if __name__ == "__main__":
    main()


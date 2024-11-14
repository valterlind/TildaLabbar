
from linkedQfile import LinkedQ, Syntaxfel
from molgrafik import Molgrafik, Ruta  # Assumes Molgrafik and Ruta are in separate files


# Dictionary for atomic weights
atomic_weights = {
    "H": 1.00794, "He": 4.002602, "Li": 6.941, "Be": 9.012182, "B": 10.811, "C": 12.0107, "N": 14.0067,
    "O": 15.9994, "F": 18.9984032, "Ne": 20.1797, "Na": 22.98976928, "Mg": 24.3050, "Al": 26.9815386,
    "Si": 28.0855, "P": 30.973762, "S": 32.065, "Cl": 35.453, "K": 39.0983, "Ar": 39.948, "Ca": 40.078,
    "Sc": 44.955912, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938045, "Fe": 55.845,
    "Ni": 58.6934, "Co": 58.933195, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723, "Ge": 72.64, "As": 74.92160,
    "Se": 78.96, "Br": 79.904, "Kr": 83.798, "Rb": 85.4678, "Sr": 87.62, "Y": 88.90585, "Zr": 91.224,
    "Nb": 92.90638, "Mo": 95.96, "Tc": 98, "Ru": 101.07, "Rh": 102.90550, "Pd": 106.42, "Ag": 107.8682,
    "Cd": 112.411, "In": 114.818, "Sn": 118.710, "Sb": 121.760, "I": 126.90447, "Te": 127.60, "Xe": 131.293,
    "Cs": 132.9054519, "Ba": 137.327, "La": 138.90547, "Ce": 140.116, "Pr": 140.90765, "Nd": 144.242,
    "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.92535, "Dy": 162.500, "Ho": 164.93032,
    "Er": 167.259, "Tm": 168.93421, "Yb": 173.054, "Lu": 174.9668, "Hf": 178.49, "Ta": 180.94788, "W": 183.84,
    "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.966569, "Hg": 200.59, "Tl": 204.3833,
    "Pb": 207.2, "Bi": 208.98040, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227,
    "Th": 232.03806, "Pa": 231.03588, "U": 238.02891, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247,
    "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 265, "Db": 268,
    "Sg": 271, "Bh": 272, "Hs": 270, "Mt": 276, "Ds": 281, "Rg": 280, "Cn": 285
}


valid_atoms = set(atomic_weights.keys())

class MoleculeParser:
    def __init__(self, formula):
        self.queue = LinkedQ()
        for char in formula:
            self.queue.enqueue(char)

    def readformula(self):
        try:
            mol = self.readmol()
            if not self.queue.isEmpty():
                raise Syntaxfel(f"Felaktig gruppstart vid radslutet {self.remaining_formula()}")
            return mol  # Return the root of the molecule tree
        except Syntaxfel as e:
            print(e)
            return None

    def readmol(self):
        """Creates the <mol> structure by parsing groups and linking them in sequence."""
        first_group = self.readgroup()
        current_group = first_group

        while not self.queue.isEmpty() and self.queue.peek() != ')':
            next_group = self.readgroup()
            current_group.next = next_group
            current_group = next_group

        return first_group  # Return the head of the linked list of groups

    def readgroup(self):
        """Creates a <group> and returns a Ruta (cell) representing the group."""
        rutan = Ruta()  # Initialize a new Ruta for this group

        if self.current_char() == '(':
            self.queue.dequeue()
            rutan.down = self.readmol()  # Set down link to nested molecule
            if self.current_char() != ')':
                raise Syntaxfel(f"Saknad högerparentes vid radslutet {self.remaining_formula()}")
            self.queue.dequeue()
            rutan.num = self.readnum()  # Number following the parenthesis group
        else:
            rutan.atom = self.readatom()  # Atom in the group
            if self.current_char() and self.current_char().isdigit():
                rutan.num = self.readnum()  # Set count if there's a number after the atom
            else:
                rutan.num = 1

        return rutan

    def readatom(self):
        """Reads an atom according to <LETTER> or <LETTER><letter> rules."""
        letter = self.readletter()
        atom = letter
        if self.current_char() and self.current_char().islower():
            atom += self.queue.dequeue()
        if atom not in valid_atoms:
            raise Syntaxfel(f"Okänd atom vid radslutet {self.remaining_formula()}")
        return atom

    def readletter(self):
        """Reads a capital letter as per <LETTER> rule."""
        if self.current_char() and self.current_char().isupper():
            return self.queue.dequeue()
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {self.remaining_formula()}")

    def readnum(self):
        """Reads a number as per <num> rule and validates it."""
        num = ''
        while self.current_char() and self.current_char().isdigit():
            num += self.queue.dequeue()
        if not num or int(num) < 2:
            raise Syntaxfel("För litet tal vid radslutet " + self.remaining_formula())
        return int(num)

    def current_char(self):
        """Returns the current character without dequeueing."""
        return self.queue.peek()

    def remaining_formula(self):
        """Returns the rest of the formula as a string for error messages."""
        temp_queue = LinkedQ()
        remaining = []
        while not self.queue.isEmpty():
            char = self.queue.dequeue()
            remaining.append(char)
            temp_queue.enqueue(char)
        self.queue = temp_queue
        return ''.join(remaining)

def weight(mol):
    """Calculates the weight of the molecule recursively."""
    if mol is None:
        return 0
    total_weight = 0
    if mol.atom != "()":  # If this is an atom node
        atom_weight = atomic_weights.get(mol.atom, 0)
        total_weight += atom_weight * mol.num
    if mol.down:  # If this node has a substructure
        total_weight += mol.num * weight(mol.down)
    total_weight += weight(mol.next)  # Add weight of the next node
    return total_weight

def main():
    mg = Molgrafik()  # Initialize Molgrafik for drawing
    while True:
        formula = input("Enter a chemical formula (# to quit): ")
        if formula == '#':
            break
        parser = MoleculeParser(formula)
        mol = parser.readformula()  # Parse the formula and get the molecule tree
        if mol:
            mg.show(mol)  # Display the molecule structure in GUI
            print(f"Molecular weight: {weight(mol):.2f}")  # Print the molecular weight

if __name__ == "__main__":
    main()

import unittest
import re

class Syntaxfel(Exception):
    def __init__(self, meddelande):
        super().__init__(meddelande)

def kontrollera_molekyl(molekyl):
    if not molekyl:
        raise Syntaxfel("Molekyl får inte vara tom.")
    kontrollera_atom(molekyl)

def kontrollera_atom(atom):
    match = re.match(r"^([A-Z][a-z]?)(\d*)$", atom)
    if not match:
        raise Syntaxfel("Saknad stor bokstav vid radslutet: " + atom)

    # Kontrollera numret, det ska finnas om match.group(2) inte är tomt
    num_part = match.group(2)  # Tar numret (om det finns)
    if num_part and not re.match(r"^[2-9][0-9]*$", num_part):
        raise Syntaxfel("För litet tal vid radslutet: " + num_part)

def kontrollera_num(num):
    if not re.match(r"^[2-9][0-9]*$", num):  # Kontrollera att det är ett giltigt nummer
        raise Syntaxfel("För litet tal vid radslutet: " + num)

def main():
    while True:
        molekyl = input()
        if molekyl == "#":
            break
        try:
            kontrollera_molekyl(molekyl)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)

if __name__ == "__main__":
    main()


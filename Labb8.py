import unittest


class Syntaxfel(Exception):
    def __init__(self, meddelande):
        super().__init__(meddelande)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.__first.data
        self.__first = self.__first.next
        return data

    def isEmpty(self):
        return self.__first is None

    def peek(self):
        if self.isEmpty():
            return None
        return self.__first.data


def read_molekyl(queue):
    read_atom(queue)
    if queue.peek() and queue.peek().isdigit():
        read_num(queue)


def read_atom(queue):
    read_letter(queue)
    if queue.peek() and queue.peek().islower():
        read_lower_letter(queue)


def read_letter(queue):
    if not queue.peek() or not queue.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + ''.join(rester(queue)))
    queue.dequeue()


def read_lower_letter(queue):
    if queue.peek() and queue.peek().islower():
        queue.dequeue()


def read_num(queue):
    num = ''
    while queue.peek() and queue.peek().isdigit():
        num += queue.dequeue()
    if num.startswith("0"):
        raise Syntaxfel("För litet tal vid radslutet " + num)
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet " + num if int(num) > 0 else '')


def rester(queue):
    remaining = []
    while queue.peek():
        remaining.append(queue.dequeue())
    return remaining


def main():
    while True:
        molekyl = input("Ange en molekyl: ")
        if molekyl == "#":
            break
        queue = LinkedQ()
        for char in molekyl:
            queue.enqueue(char)
        try:
            read_molekyl(queue)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)


if __name__ == "__main__":
    main()


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
            "Cr0": "För litet tal vid radslutet 0",
            "Pb1": "För litet tal vid radslutet 1",
            "H01011": "För litet tal vid radslutet 01011",
            "K01": "För litet tal vid radslutet 01"
        }
        for molekyl, expected_message in fel_molekyler.items():
            queue = LinkedQ()
            for char in molekyl:
                queue.enqueue(char)
            with self.assertRaises(Syntaxfel) as cm:
                read_molekyl(queue)
            self.assertEqual(str(cm.exception), expected_message)


unittest.main(argv=[''], verbosity=2, exit=False)


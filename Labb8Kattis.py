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
        raise Syntaxfel("För litet tal vid radslutet " + ''.join(rester(queue)))
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet " + ''.join(rester(queue)))


def rester(queue):
    remaining = []
    while queue.peek():
        remaining.append(queue.dequeue())
    return remaining


def main():
    while True:
        molekyl = input()
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


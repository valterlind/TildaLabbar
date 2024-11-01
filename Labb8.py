from linkedQfile import Syntaxfel, LinkedQ


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
    if num == "1":
        raise Syntaxfel("För litet tal vid radslutet")
    elif num.startswith("0") or int(num) < 2:
        remaining = num.lstrip("0")
        raise Syntaxfel("För litet tal vid radslutet " + remaining)


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


from linkedQFile import LinkedQ
from bintreeFile import Bintree


def create_tree(filename):
    '''Skapar ett binärträd av ordfilen'''
    global svenska
    svenska = Bintree()
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            word = row.strip()  # Tar bort eventuella radbrytningar
            if word not in svenska:  # Kontrollerar om ordet redan finns i trädet
                svenska.put(word)  # Lägger till ordet i trädet

    return svenska


def makechildren(startord, q, gamla, target):
    letters = "abcdefghijklmnopqrstuvwxyzåäö"
    startord = str(startord)

    for i in range(0, len(startord)):
        for letter in letters:
            if letter != startord[i]:
                child = startord[:i] + letter + startord[i + 1:]
                if child == target:  # väg till slutord funnen
                    print(f"Det finns en väg till {target}")
                    quit()
                if child in svenska and child not in gamla:
                    q.enqueue(child)
                    gamla.put(child)


def main():
    q = LinkedQ()

    gamla = Bintree()

    create_tree("word3.txt")

    startord = input("Startord: ")
    if startord in svenska:
        q.enqueue(startord)
        gamla.put(startord)
    else:
        print("Ej giltigt ord")
        quit()
    target = input("Slutord: ")
    if target not in svenska:
        print("Slutordet finns inte i ordlistan")
        quit()

    while not q.isEmpty():
        node = q.dequeue()
        makechildren(node, q, gamla, target)
    print(f"Det finns ingen väg till {target}")


if __name__ == "__main__":
    main()

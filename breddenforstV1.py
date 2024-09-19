from bintreeFile import Bintree


def create_tree(filename):
    '''Skapar ett binärträd av ordfilen'''
    global svenska
    svenska = Bintree()
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            word = row.strip()
            if word not in svenska:
                svenska.put(word)
    return svenska


def makechildren(startord):
    '''går igenom alla sätt att byta bokstav i startordet'''
    letters = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla = Bintree()
    startord = str(startord)
    for i in range(0, len(startord)):
        for letter in letters:
            if letter != startord[i]:
                child = startord[:i] + letter + startord[i + 1:]
                if child in svenska and child not in gamla:
                    print(child)
                    gamla.put(child)


def main():
    create_tree("word3.txt")

    startord = input("Startord: ")
    if startord not in svenska:
        print("Inte ett giltigt ord")
        quit()
    slutord = input("Slutord: ")

    makechildren(startord)


if __name__ == "__main__":
    main()

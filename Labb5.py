from linkedQFile import LinkedQ
from bintreeFile import Bintree

# Initiera ordlistor och kö
svenska = Bintree()
gamla = Bintree()
q = LinkedQ()


class ParentNode:
    '''Klass för att hålla ord och dess föräldranoder'''
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

    def write_chain(self):
        '''Skriver ut ordkedjan från startord till slutord'''
        if self.parent:
            self.parent.write_chain()
        print(self.word)


class SolutionFound(Exception):
    '''Undantag för när en lösning hittats'''
    pass


def read_input():
    '''Tar in start- och slutord från användaren'''
    startord = ParentNode(input("Startord: "))
    slutord = input("Slutord: ")
    return startord, slutord


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


def generate_children(node):
    '''Genererar alla barn genom att byta ut bokstäverna i ett ord'''
    for i in range(len(node.word)):
        for letter in "abcdefghijklmnopqrstuvxyzåäö":
            child_word = node.word[:i] + letter + node.word[i + 1:]
            if child_word in svenska and child_word not in gamla and child_word != node.word:
                gamla.put(child_word)
                child_node = ParentNode(child_word, node)
                q.enqueue(child_node)


def main():
    startord, slutord = read_input()  # Läs start- och slutord
    create_tree("word3.txt")  # Läs in ordlistan från fil
    q.enqueue(startord)  # Lägg till startordet i kön
    gamla.put(startord.word)  # Lägg till startordet i gamla för att undvika att besöka det igen

    try:
        while not q.isEmpty():
            current_node = q.dequeue()  # Plocka ut första noden i kön
            if current_node.word == slutord:  # Om vi hittat slutordet
                print("Här kommer ordkedjan:")
                current_node.write_chain()  # Skriv ut ordkedjan
                raise SolutionFound  # Avbryt sökningen
            generate_children(current_node)  # Generera barn för nuvarande ord
    except SolutionFound:
        pass
    else:
        print("Det finns ingen väg från", startord.word, "till", slutord)


if __name__ == "__main__":
    main()

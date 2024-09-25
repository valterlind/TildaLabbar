from linkedQFile import LinkedQ
from bintreeFile import Bintree

ordlistan = Bintree()
gamla = Bintree()
q = LinkedQ()

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self):
        if self.parent == None:
            print(self.word)
        else:
            self.parent.writechain()
            print(self.word)

class SolutionFound(Exception):
    pass

def inmatning():
    startord = ParentNode(input("Startord: "))
    slutord = input("Slutord: ")
    return startord, slutord

def läs_fil():
    with open("word3.txt", "r", encoding="utf-8") as ordfil:
        for rad in ordfil:
            ordet = rad.strip()
            if ordet not in ordlistan:
                ordlistan.put(ordet)
            else:
                gamla.put(ordet)
    return ordlistan

def makechildren(nod, q):
    for i in range(len(nod.word)):
        for bokstav in "abcdefghijklmnopqrstuvxyzåäö":
            barn = nod.word[:i] + bokstav + nod.word[i + 1:]
            if barn in ordlistan:
                if barn not in gamla and barn != nod.word:
                    gamla.put(barn)
                    barn = ParentNode(barn)
                    barn.parent = nod
                    q.enqueue(barn)

def main():
    startord, slutord = inmatning()
    läs_fil()
    gate = False
    q.enqueue(startord)
    makechildren(startord, q)
    while not q.isEmpty():
        nod = q.dequeue()
        if nod != startord:
            makechildren(nod, q)
        if nod.word == slutord:
            print("Här kommer ordkedjan:")
            nod.writechain()
            gate = True
            SolutionFound()
    if gate != True:
        print("Det finns inte någon väg från", startord.word, "till", slutord)

if __name__ == "__main__":
    main()

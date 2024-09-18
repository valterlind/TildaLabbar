from linkedQFile import LinkedQ
from bintreeFile import Bintree

ordlistan = Bintree()
gamla = Bintree()
q = LinkedQ()

def inmatning():
    startord = input("Startord: ")
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

def makechildren(nod, q):
    for i in range(len(nod)):
        for bokstav in "abcdefghijklmnopqrstuvxyzåäö":
            barn = nod[:i] + bokstav + nod[i + 1:]
            if barn in ordlistan:
                if barn not in gamla and barn != nod:
                    gamla.put(barn)
                    q.enqueue(barn)

def main():
    startord, slutord = inmatning()
    läs_fil()
    gate = False
    q.enqueue(startord)
    makechildren(startord, q)
    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q)
        if nod == slutord:
            gate = True
    if gate == True:
        print("Det finns en väg till", slutord)
    else:
        print("Det finns inte någon väg till", slutord)

if __name__ == "__main__":
    main()

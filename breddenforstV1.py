from linkedQFile import LinkedQ
from bintreeFile import Bintree

def create_tree(filename):
    global tree # Accessible in makechildren()
    tree = Bintree()
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            word = row.strip()
            if word not in tree:
                tree.put(word)
    return tree

def makechildren(start):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    duplicates = Bintree()
    start = str(start)
    for i in range(0, len(start)):
        for char in alphabet:
            if char != start[i]:
                child = start[:i] + char + start[i+1:]
                if child in tree and child not in duplicates:
                    print(child)
                    duplicates.put(child)
    

def main():
    create_tree("word3.txt")
    
    start = input("Enter starting word: ")
    if start not in tree:
        print("Not a valid word")
        quit()
    target = input("Enter target word: ")
    
    makechildren(start)



if __name__ == "__main__":
    main()

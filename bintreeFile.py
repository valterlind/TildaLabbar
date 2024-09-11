class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left  = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


 def putta(p, newvalue):
     # Funktion som gör själva jobbet att stoppa in en ny nod

 def finns(p,value):
     # Funktion som gör själva jobbet att söka efter ett värde

 def skriv(p):
     # Funktion som gör själva jobbet att skriva ut trädet

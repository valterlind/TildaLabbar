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

#Benjamin och hugos 
def putta(current, newvalue):
    '''Adds new value to the tree'''
    if current is None:
        current = Node(newvalue)
    if newvalue < current.value:
        current.left = putta(current.left, newvalue)
    elif newvalue > current.value:
        current.right = putta(current.right, newvalue)
    return current


def finns(current, value):
    if current is None:
        return False
    elif value == current.value:
        return True
    elif value < current.value:
        return finns(current.left, value)
    elif value > current.value:
        return finns(current.right, value)
    


def skriv(current):
    '''Prints out the tree inorder'''
    if current is not None:
        skriv(current.left)
        print(current.value, end=" ")
        skriv(current.right)

def test():
    tree = Bintree()
    tree.put(32)
    tree.put(12)
    tree.put(45)
    tree.write()
    print(5 in tree)
    print(12 in tree)
    tree.put(45)
    tree.write()


if __name__ == "__main__":
    test()

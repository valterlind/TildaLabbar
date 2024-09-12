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
    '''Lägger till ett nytt värde i trädet'''
    if p is None:
        return Node(newvalue)
    if newvalue < p.value:
        p.left = putta(p.left, newvalue)
    elif newvalue > p.value:
        p.right = putta(p.right, newvalue)
    return p


def finns(p, value):
    while p is not None:
        if value == p.value:
            return True
        elif value < p.value:
            p = p.left
        else:
            p = p.right
    return False


def skriv(p):
    '''Skriver ut trädet i inorder'''
    if p is not None:
        skriv(p.left)
        print(p.value, end=" ")
        skriv(p.right)

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

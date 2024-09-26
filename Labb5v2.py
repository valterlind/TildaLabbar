class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
def writechain(node):
    '''prints out the entire path for a target word'''
    if node.parent is not None: #base case
        writechain(node.parent)
    print(node.word)    

def create_tree(filename):
    '''Creates a binary search tree of swedish words'''
    global tree #Global so accessible to makechildren()
    tree = Bintree()
    
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            word = row.strip()
            if word not in tree:
                tree.put(word)
                
    return tree

def makechildren(start, q):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    word = start.word
    
    for i in range(0, len(word)):
        for char in alphabet:
            if char != word[i]: # Only new words
                child = word[:i] + char + word[i+1:]
                if child == target: #Target found?
                    writechain(ParentNode(child, start))
                    quit()
                if child in tree and child not in duplicates: #Valid words and no duplicates
                    node = ParentNode(child, start)
                    q.enqueue(node)
                    duplicates.put(child)

def main():
    q = LinkedQ() # Queue to maintain breadth-first-search
    
    global duplicates
    duplicates = Bintree()
    
    create_tree("word3.txt")
    
    #Input values
    start = input("Enter starting word: ")
    if start in tree:
        start_node = ParentNode(start)
        q.enqueue(start_node)
        duplicates.put(start_node.word)
    else:
        print("Not a valid word")
        quit()
    global target
    target = input("Enter target word: ")
    
    # Initiate loop to find target word until queue of children is empty
    while not q.isEmpty():
        node = q.dequeue()
        makechildren(node,q)
    print(f"Det finns ingen väg till {target}")



if __name__ == "__main__":
    main()

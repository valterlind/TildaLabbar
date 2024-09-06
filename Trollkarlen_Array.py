from ArrayQFile import ArrayQ

def main():
    kort = (input('Kort: '))
    lista = (kort.split(sep=' '))

    q = ArrayQ()

    for obj in lista:
        q.enqueue(int(obj))

    mystring = []

    while q.isEmpty() == False:
        q.enqueue(q.dequeue())
        mystring.append(q.dequeue()) 
    
    print(*mystring, sep=' ')

main()

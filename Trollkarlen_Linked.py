from linkedQFile import LinkedQ

def main():
    kort = (input('Kort: '))
    lista = (kort.split(sep=' '))

    q = LinkedQ()

    for obj in lista:
        q.enqueue(int(obj))

    mystring = []

    while q.isEmpty() == False:
        q.enqueue(q.dequeue())
        mystring.append(q.dequeue()) 
    
    print(*mystring, sep=' ')

main()

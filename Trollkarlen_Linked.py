
from linkedQFile import LinkedQ

def main():
    kort = (input('Kort: '))
    tmp = (kort.split(sep=' '))
    lista = [int(obj) for obj in tmp]

    q = LinkedQ(lista)
    mystring = []

    while q.isEmpty() == False:
        q.enqueue(q.dequeue())
        mystring.append(q.dequeue()) 
    
    print(*mystring, sep=' ')

main()

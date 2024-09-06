
from linkedQFile import LinkedQ

def main():
    kort = (input('Kort: '))
    tmp = (kort.split(sep=' '))
    lista = [int(obj) for obj in tmp]

    print(lista)

    q = ArrayQ(tmp)
    mystring = []

    while q.isEmpty() == False:
        q.enqueue(q.dequeue())
        mystring.append(q.dequeue()) 
    
    print(mystring)

main()

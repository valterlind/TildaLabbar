from linkedQFile import LinkedQ
import sys


def main():
    #indata = (input('Kort: '))
    indata = sys.stdin.readline()
    lista = (indata.split(sep=' '))

    q = LinkedQ()

    for obj in lista:
        q.enqueue(obj)

    mystring = []

    while q.isEmpty() == False:
        q.enqueue(q.dequeue())
        mystring.append(q.dequeue()) 
    
    print(*mystring, sep=' ')

main()

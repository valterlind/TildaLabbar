class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedQ:
    def __init__(self):
        self.__first = None  #håller reda på första noden i kön
        self.__last = None  #pekar ut sjsta  noden i kön

    def enqueue(self, add):
        '''lägger till element sist i kön'''
        tmp = Node(add)
        if self.isEmpty():
            self.__first = tmp
            self.__last = tmp
        else:
            self.__last.next = tmp
            self.__last = tmp

    def dequeue(self):
        '''Plockar ut och returnerar det första elementet i kön'''
        if self.isEmpty():
            return None
        else:
            tmp = self.__first.data
            self.__first = self.__first.next
            return tmp

    def isEmpty(self):
        '''Returnerar true om kön är tom'''
        return self.__first == None





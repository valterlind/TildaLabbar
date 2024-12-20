class Syntaxfel(Exception):
    pass



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.__first.data
        self.__first = self.__first.next
        return data

    def isEmpty(self):
        return self.__first is None

    def peek(self):
        if self.isEmpty():
            return None
        return self.__first.data

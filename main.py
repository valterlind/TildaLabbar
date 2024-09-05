from array import array

class ArrayQ:
    def __init__(self, data = []):
        self.__data = array('I', data)

    def isEmpty(self):
        return len(self.data) == 0
   
    def enqueue(self, obj):
        self.__data.append(obj)
    
    def dequeue(self):
        return self.__data.pop(0)


def arrayQ_testing():
    '''Testing for ArrayQ class'''
    print("\nArrayQ testing:\n")
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print('OK')
    else:
        print("FAILED")

arrayQ_testing()

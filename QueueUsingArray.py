class Queue:

    def __init__(self):
        self.__arr = []
        self.__front = -1
        self.__count = 0

    def enqueue(self,data):

        if self.__front == -1:
            self.__arr.append(data)
            self.__front = 0
            self.__count += 1
        else:
            self.__arr.append(data)
            self.__count += 1


    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        ele = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return ele

    def isEmpty(self):
        if self.__count == 0:
            return True
        else:
            return False

    def size(self):
        return self.__count


q = Queue()
q.enqueue(10)
q.enqueue(25)
q.enqueue(35)
print(q.size())
print(q.dequeue())
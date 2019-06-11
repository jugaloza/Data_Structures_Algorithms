class Stack:
    def __init__(self):
        self.__arr = []
        self.__c = 0

    def push(self,data):
        self.__arr.append(data)
        self.__c += 1

    def pop(self):
        self.__c -= 1
        return self.__arr.pop()

    def top_index(self):
        return len(self.__arr)-1

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def size(self):
        return self.__c



class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.count = 0

    def enqueue(self,data):
        self.s1.push(data)
        self.count += 1

    def dequeue(self):
        while self.s1.top_index() != 0:
            self.s2.push(self.s1.pop())

        ele = self.s1.pop()
        self.count -= 1

        while self.s2.isEmpty() is False:
            self.s1.push(self.s2.pop())

        return ele

    def size(self):
        return self.count





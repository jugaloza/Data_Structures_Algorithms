class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.__head = None
        self.count = 0

    def push(self,item):
        if self.head is None:
            new = Node(item)
            self.head = new
            self.count += 1
        else:
            new = Node(item)
            new.next = self.head
            self.head = new
            self.count += 1

    def pop(self):
        if self.__head is None:
            return 0
        else:
            if self.head.next is not None:
                print(self.__head.data)
                self.__count -= 1
                self.__head = head.next
            else:
                print(self.head.data)
                self.__size -= 1
                self.__head = None

        return

    def top(self):
        if isEmpty() is True:
            return 0
        else:
            print(self.__head.data)

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0







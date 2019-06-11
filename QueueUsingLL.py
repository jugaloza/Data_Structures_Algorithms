class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self,data):
        new = Node(data)
        if self.front is None:
            self.front = new
            self.rear = new
            self.count += 1

        else:
            self.rear.next = new
            self.rear = self.rear.next
            self.count += 1

    def dequeue(self):
        if self.isEmpty() is True:
            print("Queue is empty")

        ele = self.front.data
        self.front = self.front.next
        self.count -= 1
        return ele

    def size(self):
        return self.count

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False





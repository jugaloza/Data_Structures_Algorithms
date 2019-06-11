class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty() is True:
            return

        return self.data.pop()




    def top(self):
        if self.isEmpty():

            return
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0


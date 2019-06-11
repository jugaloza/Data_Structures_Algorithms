class Stack:
    def __init__(self):
        self.__arr = []

    def push(self,data):
        self.__arr.append(data)


    def pop(self):
        return self.__arr.pop()

    def top(self):
        return self.__arr[len(self.__arr)-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__arr)

def countBracketReversals(string):
    s = Stack()
    for i in string:
        if i == '{':
            s.push(i)
        else:
            if s.isEmpty() is False and s.top() == '{':
                s.pop()
            else:
                s.push(i)
    c = 0
    while s.isEmpty() is False:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            c += 2
        else:
            c += 1

    return c


string = input()
ans = countBracketReversals(string)
print(ans)
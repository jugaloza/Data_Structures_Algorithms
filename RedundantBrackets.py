
def checkRedundant(string):
    s = []

    for i in string:
        c = 0
        if i != ')':
            s.append(i)
        else:
            while len(s) != 0 and s.pop() != '(':
                c += 1
            if c == 0:
                return True
    return False






#### Implement Your Code Here


string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')





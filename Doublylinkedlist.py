class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def inputll():
     head = None
     list = input().split()
     for data in list:
         data = int(data)
         if data == -1:
             break
         else:
             newNode = Node(data)
             if head == None:
                 head = newNode
                 head.next = None
                 head.prev = None
                 tail = newNode
             else:
                 newNode.next = None
                 newNode.prev = tail
                 tail.next = newNode
                 tail = tail.next

     return head


def printlist(head):
    while head != None:
        print(head.data,end=" ")
        head = head.next
def insertatithpos(head,i,data):
    newNode = Node(data)
    count = 0
    if i == 0:
        newNode.next = head
        newNode.prev = None
        head.prev = newNode
        head = newNode
        return head
    else:
        curr = head
        while count < i:
            curr = curr.next
            count += 1
        temp = curr.next
        newNode.next = temp
        temp.prev = newNode
        newNode.prev = curr
        curr.next = newNode
        return head




ll = inputll()
printlist(ll)
printlist(insertatithpos(ll,1,1))


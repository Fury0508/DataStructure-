class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,newValue):
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode

    def printData(self):
        tmp = self.head
        while tmp:
            print(tmp.data,tmp.next)
            tmp = tmp.next


llist = LinkedList()
llist.push(4)
llist.push(5)
llist.printData()
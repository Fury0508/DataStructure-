# Node class is created to create Node every time when we want to add new node in linked list
from tempfile import tempdir


class Node:
    def __init__(self,data):
        self.data = data
        #Next in the starting is always null as in the starting it is a seperate node we have to merge with the linked list
        self.next = None

#This  linked list class has a constructor which consist of head which will be null at starting point 
# After putting the value the head will contain the value
class LinkedList:
    def __init__(self):
        self.head = None

    #Push will put value in the empty linked list so that we can begin the list
    def push(self,newValue):
        #created a new block because we need 
        #a new node
        newNode = Node(newValue)
        #whatever value pointing out the head that
        #should point out the new node next
        newNode.next = self.head
        #redirect the head to new node
        self.head = newNode

    #InstertAt will put value at specific positon 
    def insertAt(self,prevNode,newValue):
        if prevNode is None:
            print("Previous node seems to be empty")
        
        newNode = Node(newValue)
        newNode.next = prevNode.next
        prevNode.next = newNode

    # append Data means it will put value at a the last after checking the conditons
    def appendData(self,newValue):
        newNode = Node(newValue)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def printList(self):
        tmp = self.head
        while tmp :
            print(tmp.data,tmp.next)
            tmp = tmp.next

    def deleteNode(self,key):
        #temp is key we are looking through
        #case1
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        #need to check this second case again
        #case2
        while temp is not None:
            if temp.data == key:
                break
            prev == temp
            temp.next
        
        #case3
        if temp == None:
            return
        #Prev is previous node of temp
        prev.next = temp.next
        temp = None

    def deleteTotalList(self):
        curr = self.head
        while curr:
            prev = curr.next
            del curr.data

            curr = prev
    
    def getNodeCount(self,node):
        if not node:
            return 0
        else:
            return 1 + self.getNodeCount(node.next)
    
    def getCount(self):
        return self.getNodeCount(self.head)
if __name__ == '__main__':
    llist = LinkedList()
    llist.appendData(3)
    llist.push(4)
    llist.push(5)
    llist.insertAt(llist.head,6)
    llist.deleteNode(5)

    llist.printList()
#create a class node 
# node consists of two things - data and next pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create a class for LINKED LIST
#which contains Head pointer

class LinkedList:
    def __init__(self):
        self.head = None
    
    #create an function to add node to linked list 
    def insert(self,newdata):
        #create a new node by giving new data
        newnode = Node(newdata)

        #check if head pointer is NONE or It is pointing to someone
        #if it is none - assign the newnode to head
        if self.head == None:
            self.head = newnode
        else:
            #if head is already pointing to someone then traverse and find the last node and last.next = none
            #put the newnode to the last node.
            last = self.head
            while (last.next):
                last = last.next
            last.next = newnode
    
    
    #create a function to print our linked list
    #traverse through linked list and print data
    def PrintLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next

def helperFunc(myll,current,previous):
    if current.next is None:
        myll.head=current
        current.next = previous
        return
    
    next = current.next
    current.next = previous

    helperFunc(myll,next,current)    

def Reversefunc(myll):
    if myll.head == None:
        return
    
    helperFunc(myll,myll.head,None)


#create an object of linked list
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
Reversefunc(linkedlist)
linkedlist.PrintLinkedList()
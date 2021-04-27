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
    
    #return the length of the list
    def lengthOfLL(self):
        current=self.head
        length = 0
        while current:
            length+=1
            current=current.next
        return length
    #-----------------------------------------------------------
    def PrintMiddle(self):
        if self.lengthOfLL() >1:
            current = self.head
            m=self.lengthOfLL()//2
            m=m+1
            for i in range(m):
                if i==m-1:
                    print(current.data)
                current=current.next
        else:
            print("there is no middle node.")
    #---------------------------------------------------------------------

#create an object of linked list
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)



linkedlist.PrintMiddle()
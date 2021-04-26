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
    
    #writing function to remov element appearing single time or multiple time 
    def RemoveElement(self,val):
        #if we have to remove element present at the head node
        if self.head.data==val:
            self.head=self.head.next
        
        #creating three pointers - prev | current | nxt 
        #initially all pointing at head node
        nxt=self.head
        prev,current = nxt,self.head

        #iterating using current node
        while current:
            #nxt will contain the next node
            nxt=current.next
            
            #if we got the value then we put the next node to prev node -- now link of prev to current node 
            #has been broken. But next of cuurent still poitning to next so we assign next to the current.
            if current.data==val:
                prev.next=nxt
            else:
                #prev shifted towards right
                prev = current
            current=nxt
        return nxt



    #create a function to print our linked list
    #traverse through linked list and print data
    def PrintLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next

#create an object of linked list
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(6)
linkedlist.insert(2)
linkedlist.insert(6)
linkedlist.RemoveElement(1)
linkedlist.PrintLinkedList()
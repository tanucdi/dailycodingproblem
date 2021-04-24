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
    
    #----------------------------------------------------------CREATED
    #create a function to reverse list for that we have to change the direction of next of node to prev
    #for that we create a prevnode in which we start putting the nodes through iterating the linked list.
    def ReverseLinkedList(self):
        previous = None
        while self.head:
            #to store the current head #1
            currentnode = self.head
            #now change the head  #1 --> #2
            self.head = self.head.next
            #now current node is #1 and we have to add the address of previous node to its next
            currentnode.next = previous
            #now current node has #1 and in its next previous node i.e. #2 | so append the currentnode to prev.
            previous = currentnode
        
        #now the linked list is #1 <-- #2 <-- #3 <-- #4 <-- #5 <-- HEAD (we put the head pointer to last)
        #and last head contain the next of #4 and so on
        self.head = previous
    
    
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
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.ReverseLinkedList()
linkedlist.PrintLinkedList()
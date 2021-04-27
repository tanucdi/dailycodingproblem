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
    
    def ReverseinK(self, head, k):
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
 
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.ReverseinK(next, k)
 
        # prev is new head of the input list
        return prev

    
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
linkedlist.head=linkedlist.ReverseinK(linkedlist.head,2)
linkedlist.PrintLinkedList()
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
    
    #return the length of the list
    def LengthOfList(self):
        current=self.head
        length = 0
        while current:
            length+=1
            current=current.next
        return length
    
    def islistempty(self):
        if self.head is None:
            return True
        else:
            return False

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
    

    #create a function to insert a node at  begining 
    #change the next of newnode to head node and head node to newnode
    def HeadNodeInsert(self,newdata):
        newheadnode = Node(newdata)
        
        newheadnode.next=self.head
        self.head=newheadnode
    
    #-------------------------------------------------IT IS ADDED
    #create a function to insert a node at particular position
    #for that we have to create a variable which stores previous node and
    #  position starts from 0 to our required position

    def InsertAtPos(self,newdata,position):
        #if the position is -ve or greater than the list| so we call the length function
        if position < 0 or position >= self.LengthOfList():
            print('Invalid Position !!!!')
            return

        #if the positon is 0 then we have to call the insertnode func
        if position == 0:
            self.HeadNodeInsert(newdata)
            return

        #create a current head node and current position through which we can iterate
        newnode = Node(newdata)
        currentnode = self.head
        currentpos = 0

        #traverse throgh the linked list
        while True:
            if currentpos == position:
                #now we have to add previos node next to new node and next of new node to current node
                previousnode.next = newnode
                newnode.next = currentnode 
                #we have to break it coz we have added the node
                break

            #we have to store the previous node and increase the current node and position
            previousnode = currentnode
            currentnode = currentnode.next
            currentpos += 1

    #deletinh the linked list
    def DeleteList(self):
        if self.head != None:
            self.head=None
            print("Linked List Destroyed.")
        else:
            print("List is already Empty")
    
    #TO delte a head we assign the self.head.next to self.head but before this we store it in previous head.
    def DeleteHead(self):
        if self.islistempty() is False:
            previoushead = self.head
            self.head = self.head.next
            previoushead.next = None
        else:
            print('List is empty. Delete failed.!!!')

    #create Function to delete a node at the end. We have to traverse through the end then 
    #change the previous node next to None. THAts it.
    def DeleteAtEnd(self):
        #if the linked list is empty
        if self.head == None:
            print('There is nothing to delete')
            return

        #if the linked list contains only head then how can we delete an end node
        if self.LengthOfList() == 1:
            print("there is only head node then how can we delete an end node")
            return

        #current node is the head node | now we traverse through it. and make the 2nd last node next = NONE
        currentnode = self.head
        while True:
            if currentnode.next == None:
                previousnode.next = None
                break
            previousnode = currentnode
            currentnode = currentnode.next

    #deleting a node at a particular position
    def DeleteAtPos(self,position):
        #if position is invalid
        if position < 0 or position >= self.LengthOfList():
            print('Invalid Position !!!!')
            return

        if self.islistempty() is False:
            #if position is zero
            if position == 0:
                self.DeleteHead()
                return

            currentnode = self.head
            currentpos = 0

            while True:
                if currentpos == position:
                    #we have to make the next of previous node = next of cuurent node 
                    #and make the next of current to NONE.
                    previousnode.next = currentnode.next
                    currentnode.next = None
                    break

                previousnode = currentnode
                currentnode = currentnode.next
                currentpos += 1
        else:
            print('Linked list is Empty. Try Inserting a node.')

    #create a function to print our linked list
    #traverse through linked list and print data
    def PrintLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next


#create an object of linked list
linkedlist = LinkedList()
linkedlist.HeadNodeInsert(1)
linkedlist.insert(3)
linkedlist.InsertAtPos(2,1)
linkedlist.DeleteAtPos(1)
linkedlist.DeleteAtEnd()
linkedlist.DeleteHead()
linkedlist.insert(1)
linkedlist.DeleteList()
linkedlist.PrintLinkedList()
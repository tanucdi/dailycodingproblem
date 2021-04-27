class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Insert(self,val):
        newnode = Node(val)
        if self.head ==None:
            self.head=newnode
        else:
            last = self.head
            while last.next:
                last=last.next
            last.next =newnode
    

    def PrintList(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next


def MergeList(headA,headB):
# A dummy node to store the result
    dummylist=LinkedList()
    dummyNode = Node(0)
  
    # Tail stores the last node
    tail = dummyNode
    while True:
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
  
        # Advance the tail
        tail = tail.next
  
    # Returns the head of the merged list
    dummylist.head=dummyNode.next
    return dummylist

l1=LinkedList()
l2=LinkedList()
l1.Insert(1)
l1.Insert(2)
l1.Insert(4)
l2.Insert(1)
l2.Insert(3)
l2.Insert(5)
l2.Insert(6)
#to call the function
l=MergeList(l1.head,l2.head)
l.PrintList()
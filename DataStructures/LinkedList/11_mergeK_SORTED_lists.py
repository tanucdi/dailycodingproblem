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

def PrintList(l):
        current = l.head
        while current:
            print(current.data)
            current=current.next

def MergeList(headA,headB):
# A dummy node to store the result
    #Program is returning a node object but we have to take the list object thats why storing the next object in
    # the head of list object
    dummylist = LinkedList()
    dummyNode = tail = Node(0)
  
    # Tail stores the last nod
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
        # head a-   5
        # head b -  6 7
        # tail - 1 1  5 6 7
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

def MergeKlist(l):
    if len(l)==0:
        return None
    while len(l)>1:
        mergedlists=[]
        for i in range(0,len(l),2):
            l1=l[i]
            l2=l[i+1] if (i+1) < len(l) else None
            mergedlists.append(MergeList(l1.head,l2.head))
        l=mergedlists
    return l[0]

l1=LinkedList()
l2=LinkedList()
l3=LinkedList()
l4=LinkedList()
l1.Insert(1)
l1.Insert(13)
l1.Insert(13)
l2.Insert(4)
l2.Insert(5)
l2.Insert(6)
l2.Insert(7)
l3.Insert(8)
l3.Insert(9)
l3.Insert(10)
l4.Insert(11)
l4.Insert(12)
l4.Insert(13)
#to call the function
l=MergeKlist([l1,l2,l3,l4])
# l.PrintList()
PrintList(l)
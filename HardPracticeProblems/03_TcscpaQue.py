#######################input 1##########################
# 5
# 101
# To kill a Mockingbird
# Harper Lee
# Novel
# 120
# available
# 102
# One Hundred Years of Solitude
# Gabriel Garcia Marquez       
# Novel
# 100
# unavailable
# 103
# Go Set A Watchman
# Harper Lee
# Novel
# 200
# available
# 104
# Python Programming
# Reema Thareja
# Programming
# 150
# available
# 105
# Let Us C++
# Yashavant Kanetkar
# Programming
# 300
# available
# one hundred years of solitude
# novel
# tanishk
# Book not found
# Author not found

###################### input 2###########################
# 5
# 101
# To kill a Mockingbird
# Harper Lee
# Novel
# 120
# available
# 102
# One Hundred Years of Solitude
# Gabriel Garcia Marquez       
# Novel
# 100
# unavailable
# 103
# Go Set A Watchman
# Harper Lee       
# Novel
# 200
# available
# 104
# Python Programming
# Reema Thareja
# Programming
# 150
# available
# 105
# Let Us C++
# Yashavant Kanetkar
# Programming
# 300
# available
# Let Us C++
# Programming
# Harper Lee

class Book:
    def __init__(self,bookid,booktitle,authorname,booktype,bookprice,status):
        self.bookid=bookid
        self.booktitle=booktitle
        self.authorname=authorname
        self.booktype=booktype
        self.bookprice=bookprice
        self.status=status

class Library:
    def __init__(self,booklist):
        self.booklist=booklist
    
    def IssueBook(self,bktitle,bktype):
        for i in self.booklist:
            if i.booktitle.lower()==bktitle.lower() and i.booktype.lower()==bktype.lower() and i.status.lower()=='available':
                i.status='unavailable'
                return True
        else:
            return False

    def FindcostliestBook(self,authname):
        maxp=0
        maxpbn=None
        for i in self.booklist:
            print(i.authorname)
            if i.authorname.lower()==authname.lower():
                if i.bookprice>maxp:
                    maxp=i.bookprice
                    maxpbn=i
        
        if maxpbn==None:
            return None
        else:
            return maxpbn

testcase = int(input())
blist=[]
for i in range(testcase):
    bid = input()
    btitle = input()
    aname = input()
    btype = input()
    bprice = int(input())
    bstatus = input()
    blist.append(Book(bid, btitle, aname, btype, bprice, bstatus))

lobj = Library(blist)
inpbktitle=input()
inpbktype=input()
inpauthname=input()
a1=lobj.IssueBook(inpbktitle,inpbktype)
a2=lobj.FindcostliestBook(inpauthname)

if a1==False:
    print('Book not found')
else:
    for i in blist:
        print(i.booktitle,'->',i.status)

if a2==None:
    print('Author not found')
else:
    print(a2.booktitle)
from GetPrice import *

class UserInfo(dict): 
    d={}
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def addDetails(self,name1,age1,gender1,phone1,price1): 
        self['name'] = name1
        self['age'] = age1
        self['gender'] = gender1
        self['phone'] = phone1
        self['price'] = price1
    
    def CreateUser(self,key):
        d[key]=self
        print(d)


def createCinema(R,C):
    a = [['S' for i in range(R)] for j in range(C)]
    return a


def PrintCinema(a):
    for i in range(len(a)) : 
        for j in range(len(a[i])) : 
            print(a[i][j], end=" ")
        print()


def BuyTicket():
    print('Enter the row-seat number ?')
    print('Eg 1-3 = Row 1 and Seat 3')
    r,s=input().split('-')
    book = BookSeat(int(r),int(s),storecinema)


def BookSeat(r,s,a):
    if a[r-1][s-1]!='B':
        print('Seat Available! Want to Book ? \n Press "Y" for yes | Press "N" for no')
        res=input()
        if res!=0:
            price=TicektPrice(r,s,totalseats)
            print(f'Price for your seat is: {price}$ \n Press "Y" to Continue | Press "N" for Exit')
            resp=input()
            if resp.lower()=='y':
                name = input("Enter the Name: ")
                age = input("Enter the Age: ")
                gender = input("Enter the Gender: ")
                phone = input("Enter the Phone NO: ")
                newobj = UserInfo()
                newobj.addDetails(name,age,gender,phone,price)
                newobj.CreateUser((r,s))
                for i in range(len(a)) : 
                    for j in range(len(a[i])):
                        if i==r-1 and j==s-1:
                            a[i][j]='B'
                            print(f'Ticket Booked, Your Seat No is {r,j}')
                            return a
            else:
                return None
        else:
            return None
    else:
        print('Seat Already Booked. Kindly Choose Another One')


#---------------------------------------------------------------------------#
rows = int(input("Enter the number of rows:"))
seats = int(input("Enter the number of seats per row:"))
totalseats=rows*seats
storecinema=createCinema(rows,seats)
d={}
#----------------------------------------------------------------------------#


def Menu():
    print('1: Show the Seats')
    print('2: Buy a Ticket')
    print('3: Show Statistics')
    print('4: Show Booked Ticket User Info')
    print('0: Exit')
    print('----------')
    print('Enter Your Choice ?')
    choice=int(input())
    if choice==1:
        PrintCinema(storecinema)
        Menu()
    elif choice==2:
        BuyTicket()
        Menu()
    elif choice==7:
        print(d)

Menu()
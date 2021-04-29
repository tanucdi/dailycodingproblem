import DesignColors
import UserclassObjects
from GetPrice import *
color=DesignColors.Fonts()
class Theatre:
    def __init__(self,rows,seats):
        self.rows=rows
        self.ticketpurchased=0
        self.ticketpercentage=0
        self.currentincome=0
        self.totalseats=self.rows*seats
        self.totalincome =0
        self.users={}
        self.a = [['S' for i in range(self.rows)] for j in range(seats)]
        if self.totalseats<=60:
            self.totalincome=self.totalseats*10
        else:
            if rows%2:
                self.totalincome=(self.rows//2)*seats*10 + (self.rows//2)*seats*8
            else:
                r=self.rows//2
                y=self.rows-r
                self.totalincome=r*seats*10 + y*seats*8

    def PrintCinema(self):
        for i in range(len(self.a)) : 
            for j in range(len(self.a[i])) : 
                print(self.a[i][j], end=" ")
            print()


    def BuyTicket(self):
        print('Enter the row-seat number ?')
        print('Eg 1-3 = Row 1 and Seat 3')
        r,s=input().split('-')
        self.BookSeat(int(r),int(s))

    def BookSeat(self,r,s):
        if self.a[r-1][s-1]!='B':
            print('Seat Available! Want to Book ? \n Press "Y" for yes | Press "N" for no')
            res=input()
            if res.lower()=='y':
                price=TicektPrice(r,s,self.totalseats,self.rows)
                print(f'Price for your seat is: {price}$ \n Press "Y" to Continue | Press "N" for Exit')
                resp=input()
                if resp.lower()=='y':
                    name = input("Enter the Name: ")
                    age = input("Enter the Age: ")
                    gender = input("Enter the Gender: ")
                    phone = input("Enter the Phone NO: ")
                    newobj = UserclassObjects.UserInfo()
                    newobj.addDetails(name,age,gender,phone,price)
                    user=newobj.CreateUser((r,s))
                    self.users.update(user)
                    for i in range(len(self.a)) :
                        for j in range(len(self.a[i])):
                            if i==r-1 and j==s-1:
                                self.a[i][j]='B'
                                print(color.BOLD+color.RED+f'Ticket Booked, Your Seat No is {r,s}'+color.END)
                                self.ticketpurchased=self.ticketpurchased+1
                                self.ticketpercentage=round((self.ticketpurchased/self.totalseats)*100, 2)
                                self.currentincome=self.currentincome+price
                                return
                else:
                    return None
            else:
                return None
        else:
            print('Seat Already Booked. Kindly Choose Another One')

    def BookedTicketUserInfo(self):
        if self.users !={}:
            for i in self.users:
                print(color.BOLD + color.GREEN +'Seat No:'+color.END,i,color.BOLD + color.GREEN +'User Details:'+color.END,self.users[i])
        else:
            print('0 Users Booked Tickets Till Now.')

    def StatisticsMenu(self):
        print(color.BOLD + color.YELLOW +'Number of Purchased Tickets : '+ color.END,self.ticketpurchased)
        print(color.BOLD + color.YELLOW +'Percentage of Tickets Booked : '+ color.END,self.ticketpercentage,'%')
        print(color.BOLD + color.YELLOW +'Current Income : '+ color.END,self.currentincome,'$')
        print(color.BOLD + color.YELLOW +'Total Income : '+ color.END,self.totalincome,'$')
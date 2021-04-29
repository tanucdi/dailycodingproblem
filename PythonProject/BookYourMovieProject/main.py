from GetPrice import *
import DesignColors
import TheatreclassObjects
color = DesignColors.Fonts()

#---------------------------------------------------------------------------#
print('Lets Start With Creating The Sitting Space For The Cinema')
rows = int(input("Enter the number of rows:"))
seats = int(input("Enter the number of seats per row:"))
sc=TheatreclassObjects.Theatre(rows,seats)
#----------------------------------------------------------------------------#

print(color.BOLD + color.RED + 'WELCOME TO THE TANISHQ CINEMAS'+ color.END)
print('Which Movie Do You Want To Watch ?\nType Name')
s=input()
print('----------Audi 1 Available For',s,'Kindly Book Your Seat----------')

def Menu():
    print(color.BOLD + color.DARKCYAN +'1: Show the Seats'+ color.END)
    print(color.BOLD + color.DARKCYAN +'2: Buy a Ticket'+ color.END)
    print(color.BOLD + color.DARKCYAN +'3: Show Statistics'+ color.END)
    print(color.BOLD + color.DARKCYAN +'4: Show Booked Ticket User Info'+ color.END)
    print(color.BOLD + color.DARKCYAN +'0: Exit'+ color.END)
    print('----------')
    print('Enter Your Choice ?')
    choice=input()
    if choice=='1':
        sc.PrintCinema()
        Menu()
    elif choice=='2':
        sc.BuyTicket()
        Menu()
    elif choice=='3':
        sc.StatisticsMenu()
        Menu()
    elif choice=='4':
        sc.BookedTicketUserInfo()
        Menu()
    elif choice=='0':
        print(color.BOLD + color.GREEN +'Thank You For Visiting Tanishq Cinemas....'+ color.END)
        exit()
    else:
        print('Kindly Choose From the Given Options.')
        Menu()

Menu()
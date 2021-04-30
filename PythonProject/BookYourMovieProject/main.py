from GetPrice import *
import DesignColors
import TheatreclassObjects
color = DesignColors.Fonts()

#---------------------------------------------------------------------------#
print(color.BOLD + color.WHITE +'Lets Start With Creating The Sitting Space For The Cinema'+ color.END)
try:
    rows = int(input(color.BOLD + color.WHITE +"Enter the number of rows:"+ color.END))
    seats = int(input(color.BOLD + color.WHITE +"Enter the number of seats per row:"+ color.END))
    sc=TheatreclassObjects.Theatre(rows,seats)
except:
    print('Please Provide Number As Input')
    exit()
#----------------------------------------------------------------------------#

print(color.BOLD + color.RED + 'WELCOME TO THE TANISHQ CINEMAS'+ color.END)
print(color.BOLD + color.WHITE +'Which Movie Do You Want To Watch ?\nEnter Movie Name -'+ color.END)
s=input()
print('----------Audi 1 Available For',s.upper(),'Kindly Book Your Seat----------')

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
        print(color.BOLD + color.GREEN +'Thank You For Visiting Tanishq Cinemas | We Love To See You Again.'+ color.END)
        exit()
    else:
        print('Kindly Choose From the Given Options.')
        Menu()

Menu()
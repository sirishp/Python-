import random

class Atm:  # Added a Class

    def __init__(self,bal):
        self.bal=bal

    def __str__(self):
        return 'This is an ATM banking system'+self.bank


    def Deposit(self,bal):  # Added a Function
        values={1,5,10,20,50,100} # Set
        print('You can deposit the following denomination ',values,'notes')
        amt = float(input("Enter the amount to be deposited"))
        bal = bal + amt
        print("Your amount has been deposited sucessfully")
        print("Your Balance=", bal)
        return bal


    def Withdraw(self,bal):

        values=[5,10,20,50,100]  # List
        print(values)
        amt = eval(input("Enter the amount to be withdrawn in the following multiples\n"))


        if amt%values[0]==0 or amt%values[1]==0 or amt%values[2]==0 or amt%values[3]==0 or amt%values[4]==0:
            print('You are withdrawing$',amt)

            if bal >= amt:
                bal = bal - amt
                print("Your amount has been Withdrawn sucessfully")
                print("Your Balance=", bal)

            else :
                    print("Insufficient Balance")

        else:
            print('entered invalid amount')



        return bal

    def Balance(self,bal):


        print("Your Balance=", bal)
        return bal




print("ATM Banking")
b=(30000,25000,2000,10000,10,450000,600000)  # Tuple
bal=random.choice(b)

ob=Atm(bal)

r=open('Pin.txt','r')  # File
l=r.read().splitlines()

p=(input('Please Enter your ATM Pin'))  # Pin file
print('\nWelcome')

def main():
    if p in l:

        dic={'1':'Withdraw','2':'Deposit','3':'Balance','4':'Exit'}  # Dictionary
        print('\n')
        for i in dic:     # For Loop (Iteration Type)
            print(i,dic[i])

        ip=eval(input('Please select an option from above\n'))
        if ip==1:
            ob.Withdraw(bal)
            print('\nDo you want to make another transaction?')
            main()

        elif ip==2:
            ob.Deposit(bal)
            print('\nDo you want to make another transaction?')
            main()

        elif ip==3:
            ob.Balance(bal)
            print('\nDo you want to make another transaction?')
            main()

        elif ip==4:
            print('Thank you, please visit again')


    else:
        print('Incorrect Pin')

main()


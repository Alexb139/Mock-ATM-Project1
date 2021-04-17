#This is withdrawl and deposit functions
name = input("What is your username? \n")
allowedUsers = ['Seyi','Mike','Love','Alexandria']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove','passwordAlexandria']
allowedWithdrawals = ['$20','$50','$100','$250']
currentBalance = 1000
A = 20
B = 50
C = 100
D = 250

from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from datetime import date
today = date.today()

if(name in allowedUsers):
    password = input ("Your password? \n")
    userID = allowedUsers.index(name)
    
    if(password == allowedPassword[userID]):

        print('Welcome %s' % name)
        print('Current Time=', current_time)
        print("Today's Date:", today)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        
        
        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            print('How much would you like to withdraw?')
            print('A. $20')
            print('B. $50')
            print('C. $100')
            print('D. $250')

        selectedOption = int(input('How much would you like to withdraw?'))

        if(selectedOption == 20):
                print('take your cash')
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
        elif(selectedOption == 50):
                print('take your cash')
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
        elif(selectedOption == 100):
                print('take your cash')
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
        elif(selectedOption == 250):
                print('take your cash')
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            print('How much would you like to deposit?')
            #print('take your cash')
            print('A. $40')
            print('B. $80')
            print('C. $200')
            print('D. $350')

        if(selectedOption == 20):
                print(currentBalance + 20)
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')

        elif(selectedOption == 50):
                print(currentBalance + 50)
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')

        elif(selectedOption == 100):
                print(currentBalance + 100)
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')


        elif(selectedOption == 250):
                print(currentBalance + 250)
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
                
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            print('What issue would you like to report?')

            selectedOption = input('What is issue would you like to report?')
                print('Welcome %s' % name)
                print('Current Time=', current_time)
                print("Today's Date:", today)
                print('These are the available options:')
                print('1. Withdrawl')
                print('2. Cash Deposit')
                print('3. Complaint')
            
        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')

else:
        print('Name not found, please try again')






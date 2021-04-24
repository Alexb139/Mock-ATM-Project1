#register
# - first name, last name, password, email
# - generate user account

allowedWithdrawals = ['$20','$50','$100','$250']
# currentBalance = 1000
# A = 20
# B = 50
# C = 100
# D = 250

from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from datetime import date
today = date.today()



#login
# - account number & password

#bank operations


#Initializing the system
import random

database = {
    "0123456789" : ["Bill", "Gate", "email@email.com", "password", 1000]
} #dictionary

def init():

    
    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else: 
        print("You have selected invalid option")
        init()


def login():

    print("********** Login ***********")


    accountNumberFromUser = str(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails) 

    print ('Invalid account or password')
    login()
       


def register():

    print("******* Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    balance = 1000

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, balance ]

    print("Your Account Has been Created")
    print(" == ==== ====== ===== ===")
    print("Your account number is %d" %accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):
    # print(user)
    print("Welcome %s %s " % ( user[0], user[1] ) )
    print('Current Time=', current_time)
    print("Today's Date:", today)
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
    
    elif(selectedOption == 2):
        
        withdrawalOperation(user)
    
    elif (selectedOption == 3):

        logout()
    
    elif (selectedOption == 4):

        exit()
    
    

    
def withdrawalOperation(user):

    get_current_balance = user[4]
    print(get_current_balance)
 
    selectedOption = int(input('How much would you like to withdraw? \n'))
    # print('How much would you like to withdraw?')
    print('A. $20')
    print('B. $50')
    print('C. $100')
    print('D. $250')
    print('E. Enter Amount')

    if(selectedOption == 20):
        get_current_balance = get_current_balance - 20 
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')
        
    elif(selectedOption == 50):
        get_current_balance = get_current_balance - 50
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')
        
    elif(selectedOption == 100):
        get_current_balance = get_current_balance - 100
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')
        
    elif(selectedOption == 250):
        get_current_balance = get_current_balance - 250 
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')       

    elif(selectedOption == "E"):
        amount_to_withdraw = int(input("Enter amount to withdraw"))
        get_current_balance = get_current_balance - amount_to_withdraw
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')
    
    return bankOperation(user)


def depositOperation(user):

    get_current_balance = user[4]
    print(get_current_balance)
    
    selectedOption = int(input("How much would you like to deposit? \n"))
    #print("How much would you like to deposit?")
    print('A. $20')
    print('B. $50')
    print('C. $100')
    print('D. $250')
    print('E. Enter Amount')

    if(selectedOption == 20):
        get_current_balance = get_current_balance + 20 
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        
    elif(selectedOption == 50):
        get_current_balance = get_current_balance + 50
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        
    elif(selectedOption == 100):
        get_current_balance = get_current_balance + 100
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
            
    elif(selectedOption == 250):
        get_current_balance = get_current_balance + 250 
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
            
    elif(selectedOption == "E"):
        amount_to_deposit = int(input("Enter amount to deposit"))
        get_current_balance = get_current_balance + amount_to_deposit
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    return bankOperation(user)

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)        

def logout():
    login()

### ACTUAL BANKING SYSTEM ####


init()

## Can't seem to get the deposit function to work like the withdrawal function
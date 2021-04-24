# register
# - first name, last name, password, email
# - generate user account

allowedWithdrawals: list[str] = ['$20', '$50', '$100', '$250']
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

# login
# - account number & password

# bank operations


# Initializing the system
import random
import validation
import database

#database = {
#    "1234567890": ["Bill", "Gate", "email@email.com", "password", 1000]
#}  # dictionary


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()
    else:
        print("You have selected invalid option")
        init()


def bank_operation(user_details):
    pass


def login(user_details=None):
    print("********** Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input("What is your password? \n")

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operation(user_details)

        print('Invalid account or password')
        login()

    else:

        init()


def generation_account_number():
    pass


def register(account_number):
    print("******* Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    balance = 1000

    try:

        account_number = generation_account_number()

    except ValueError:

        print("Account generation failed due to internet connection failure")
        init()

    is_user_created = database.create(account_number[first_name, last_name, email, password, balance])

    if is_user_created:

        print("Your Account Has been Created")
        print(" == ==== ====== ===== ===")
        print("Your account number is %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()
    else:
        print("Something went wrong, please try again")
        register()


def deposit_operation():
    pass


def withdrawal_operation(user):
    pass


def bank_operation(user):
    # print(user)
    print("Welcome %s %s " % (user[0], user[1]))
    print('Current Time=', current_time)
    print("Today's Date:", today)

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()

    elif selected_option == 2:

        withdrawal_operation(user)

    elif selected_option == 3:

        logout()

    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    get_current_balance = user[4]
    print(get_current_balance)

    selected_option = int(input('How much would you like to withdraw? \n'))
    # print('How much would you like to withdraw?')
    print('A. $20')
    print('B. $50')
    print('C. $100')
    print('D. $250')
    print('E. Enter Amount')

    if selected_option == 20:
        get_current_balance = get_current_balance - 20
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')

    elif selected_option == 50:
        get_current_balance = get_current_balance - 50
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')

    elif selected_option == 100:
        get_current_balance = get_current_balance - 100
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')

    elif selected_option == 250:
        get_current_balance = get_current_balance - 250
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')

    elif selected_option == "E":
        amount_to_withdraw = int(input("Enter amount to withdraw"))
        get_current_balance = get_current_balance - amount_to_withdraw
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))
        print('take your cash')

    return bank_operation(user)


def deposit_operation(user):
    get_current_balance = user[4]
    print(get_current_balance)

    selected_option = int(input("How much would you like to deposit? \n"))
    # print("How much would you like to deposit?")
    print('A. $20')
    print('B. $50')
    print('C. $100')
    print('D. $250')
    print('E. Enter Amount')

    if selected_option == 20:
        get_current_balance = get_current_balance + 20
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    elif selected_option == 50:
        get_current_balance = get_current_balance + 50
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    elif selected_option == 100:
        get_current_balance = get_current_balance + 100
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    elif selected_option == 250:
        get_current_balance = get_current_balance + 250
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    elif selected_option == "E":
        amount_to_deposit = int(input("Enter amount to deposit"))
        get_current_balance = get_current_balance + amount_to_deposit
        user[4] = get_current_balance
        print("Your current balance is now {}".format(get_current_balance))

    return bank_operation(user)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


### ACTUAL BANKING SYSTEM ####


init()

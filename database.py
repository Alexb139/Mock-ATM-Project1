# create record
# update record
# read record
# delete record
# CRUD

# find user

import os

user_db_path = "data/user_record/"


def create(user_account_number, user_details):
    completion_state = False
    f = None

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:

        print("user already exist")
        # delete the already created file, and print out error, then return false
        # check content of file before deleting
        # delete(account_number)



    else:

        f.write(str(user_details))
        completion_state = True

    finally:

        f.close()
        return completion_state

    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then delete created file

    def read(user_account_number):

        # find user with account number
        # fetch content of the file
        try:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")

        except FileNotFoundError:

            print("User not found")

        except FileExistsError:

            print("User doesn't exist")

        finally:
            return f.readline()

    def update(user_account_number):
        print("update user record")
        # find user with account number
        # fetch the content of the file
        # update the content of the file
        # save the file
        # return true


def delete(user_account_number):
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful

            # find user with account number
            # delete the user record (file)
            # return true


# def does_email_exist(account_number, email):
    print(os.listdir(user_db_path))


# does_email_exist(1234567890, "email@email.com")
# create(1234567890, ["Bill", "Gate", "email@email.com", "password", 1000])
# delete()

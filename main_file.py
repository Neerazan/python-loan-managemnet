import admin as ad
import newcustomer as ns
import customer as cu
from os import system, name
# from time import sleep
def MainMenu():
    print('\n')
    print('-------------------------------------------------')
    print("|| MALAYSIA BANK ONLINE LOAN MANAGEMENT SYSTEM ||")
    print('-------------------------------------------------')
    print('\n')
    print("\t1. Admin Login\n")
    print("\t2. Customer Login\n")
    print("\t3. New Customer Menu\n")

    choise = int(input("Enter your choise: "))
    clear()
    if (choise == 1):
        adminLogin()
    elif (choise == 2):
        customerLogin()
    elif (choise == 3):
        ns.newCustomerMenu()
    else:

        print("\n\nInvalid option, Please try again!!\n\n")
        MainMenu()


# Admin Login Function:

def adminLogin():
    password_db = "admin@634"
    username_db = "admin"
    clear()
    print('\n')
    print("\t-----------------")
    print("\t|| ADMIN LOGIN ||")
    print("\t-----------------")
    print('\n')
    Username = input("\tUsername: ")
    Password = input("\tPassword: ")

    if(username_db == Username and password_db == Password):
        print("\n\tLogin Successful\n")
        print("\tPress any key to continue...")
        clear()
        adminMenu()
        pass
    else:
        print("Invalid Input! Try again...\n")
        adminLogin()


# customer Login Function
def customerLogin():
    uid = input("UserID: ")
    password = input("Password: ")
    with open('signup.txt', 'r') as fp:
        data = fp.readlines()
        for i in data:
            data_list = i.split(',')
            if (uid == data_list[0] and password == data_list[len(data_list) - 2]):
                print("\n\tlogin successfully\n")
                input("Press any key to continue.....\n")
                cu.customerMenu(uid)
                return
        print("Wrong ID or Password! Try again..")
        customerLogin()

# id generator
def idGenerator():
    with open("signup.txt","r") as f:
        a = f.read()
        if(a == ""):
            return "1001"
        else:
            with open("signup.txt", "r") as fp:
                while True:
                    content = fp.readline()
                    if (content == ''):
                        break
                    else:
                        list_content = content.split(',')
                        uid = list_content[0]
                return int(uid) + 1


def signUp():
    print('\n')
    print("\t------------------------")
    print("\t|| CREATE NEW ACCOUNT ||")
    print("\t------------------------\n")
    name = input("\tName: ")
    email = input("\tEmail: ")
    contact = input("\tContact: ")
    address = input("\tAddress(Name of city only): ")
    gender = input("\tGender(male/female): ")
    dob = input("\tDate of Birth: ")
    password_1 = input("\tPassword: ")
    password_2 = input("\tRetype Password: ")

    if (password_1 == password_2):
        uid = idGenerator()

        user = [str(uid), name, email, contact, address, gender, dob, password_1]
        with open("signup.txt", "a") as f:
            for item in user:
                if(item == user[len(user)-1]):
                    f.write(item + ',')
                    f.write('\n')
                else:
                    f.write(item + ',')
            print("\n")
            print("\tSuccessfully Registered.....")
            print(f"\tYour user id is {uid}, Please remember it.")
            input("\n\tpress any key to continue.....")
            clear()
            MainMenu()

    else:
        print("\tSorry, Please enter same password, Try again!!:\n")
        print("\n")
        signUp()



def adminMenu():
    print("\n")
    print("\t----------------")
    print("\t|| ADMIN MENU ||")
    print("\t----------------")
    print("\n")
    print("\t1. Approve Loan")
    print("\t2. All transaction")
    print("\t3. Search Transaction")
    print("\t4. Exit\n")

    choose = int(input("\t3Choose option: "))
    clear()

    if choose == 1:
        ad.displaLoanRequest()
    elif choose == 2:
        ad.show_all_transaction()
    elif choose == 3:
        ad.customer_transaction()
    elif choose == 4:
        MainMenu()
    else:
        print("Wrong input! Try again..")

def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


if __name__ == '__main__':
    MainMenu()
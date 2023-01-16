import admin as ad
import newcustomer as ns
import customer as cu
def MainMenu():
    print("1. Admin Login\n")
    print("2. Customer Login\n")
    print("3. New Customer Menu\n")

    choise = int(input("Enter your choise: "))
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
    Username = input("Username: ")
    Password = input("Password: ")

    if(username_db == Username and password_db == Password):
        print("Login Successful\n")
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
                print("login successfully\n")
                input("Press any key to cotinue.....\n")
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
    name = input("Name: ")
    email = input("\nEmail: ")
    contact = input("\nContact: ")
    address = input("\nAddress(Name of city only): ")
    gender = input("\nGender(male/female): ")
    dob = input("\nDate of Birth: ")
    password_1 = input("\nPassword: ")
    password_2 = input("\nRetype Password: ")

    if (password_1 == password_2):
        uid = idGenerator()

        user = [str(uid), name, email, contact, address, gender, dob, password_1]
        print(user[len(user) - 1])
        with open("signup.txt", "a") as f:
            for item in user:
                if(item == user[len(user)-1]):
                    f.write(item + ',')
                    f.write('\n')
                else:
                    f.write(item + ',')
            print("\n")
            print("Successfully Registered.....")
            print(f"Your user id is {uid}, Please remember it.")

    else:
        print("Sorry, Please enter same password, Try agin!!:\n")
        print("\n")
        signUp()



def adminMenu():
    print("1. Approve Loan")
    print("2. All transaction")
    print("3. Search Transaction")
    print("5. Exit")

    choose = int(input("Choose option: "))

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



if __name__ == '__main__':
    MainMenu()
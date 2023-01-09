
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
        # newCustomerMenu()
        pass
    else:

        print("\n\nInvalid option, Please try again!!\n\n")
        MainMenu()


# Admin Login Function:

def adminLogin():
    pass

# customer Login Function
def customerLogin():
    with open("signup.txt", "r") as fp:
        uid = input("UserID: ")
        password = input("Password: ")
        while True:
            data_db = fp.readline().split()
            if(data_db == []):
                break
            if (uid == data_db[0] and password == data_db[len(data_db) - 1]):
                print("Login Successful\n")
                customerMenu()

        print("Invalid User ID or Password please try again!!")
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
                        list_content = content.split()
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
                    f.write(item+"  ")
                    f.write('\n')
                else:
                    f.write(item + "  ")
            print("\n")
            print(f"Your user id is {uid}, Please remember it.")

    else:
        print("Sorry, Please enter same password, Try agin!!:\n")
        print("\n")
        signUp()

def customerMenu():
    print("1. Loan Details\n")
    print("2. View Transaction\n")
    print("3. Pay loan instalment\n")
    print("4. Loan status")
    print("5. Exit")

if __name__ == '__main__':
    MainMenu()
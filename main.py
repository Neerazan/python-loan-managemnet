
def MainMenu():
    print("1. Admin Login\n")
    print("2. Customer Login\n")
    print("3. New Customer Menu\n")

    choise = input("Enter your choise: ")
    if (choise == 1):
        adminLogin()
    elif (choise == 2):
        customerLogin()
    elif (choise == 3):
        newCustomerMenu()
    else:
        print("\n\nInvalid option, Please try again!!\n\n")
        MainMenu()


# Admin Login Function:

def adminLogin():
    pass

# customer Login Function

def customerLogin():
    pass

# MainMenu()

# id generator
def idGenerator():
    with open("signup.txt","r") as f:
        a = f.read()
        if(a == ""):
            return "1"
        else:
            return "2"
            # while True:
            #     count = count + 1
            #     line = f.readline()
            #     uid = line[0]
            #     if not line:
            #         break
            #
            # return uid

def newCustomerMenu():
    print("1. Check Loan details.")
    print("2. Loan calculator")
    print("3. Sign Up")
    print("4. Exit")


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
                    f.write(item)
                else:
                    f.write(item + "  ")
            print("Done")

    else:
        print("Sorry, Please enter same password, Try agin!!:\n")
        print("\n")
        signUp()


signUp()
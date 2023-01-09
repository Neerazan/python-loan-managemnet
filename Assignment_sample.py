import os
def loanCalculator():
    print('''\t\t\t\t.........Types of loan...........
    \t\t\t\t1. Education Loan (EL)
    \t\t\t\t2. Car Loan (CL)
    \t\t\t\t3. Home Loan (HL)
    \t\t\t\t4. Personal Loan (PL)
    \t\t\t\t5. Exit''')
    option = int(input("\t\t\t\tSelect your loan type: "))
    if(option == 1):
        rate = int(7)
    elif (option == 2):
        rate = int(11)
    elif (option == 3):
        rate = int(11)
    elif (option == 2):
        rate = int(7)
    elif (option == 5):
        main()
    principal = int(input("\t\t\t\tPrincipal: "))
    rate = int(7)
    time = int(input("\t\t\t\tTime: "))
    simple_interes = float((principal * time * rate) / 100)
    print("\t\t\t\tinterest = ", simple_interes)


def loan_calculaotr():
    print('''\t\t\t\t.........Types of loan...........
    \t\t\t\t1. Education Loan (EL)
    \t\t\t\t2. Car Loan (CL)
    \t\t\t\t3. Home Loan (HL)
    \t\t\t\t4. Personal Loan (PL)
    \t\t\t\t5. Exit''')
    option = int(input("\t\t\t\tSelect your loan type: "))
    if(option == 1):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(7)
        time = int(input("\t\t\t\tTime: "))
        simple_interes = (principal * time * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 2):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(11)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * time * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)


    elif (option == 3):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(11)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * time * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 4):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(7)
        time = int(input("\t\t\t\tTime: "))
        simple_interes = (principal * time * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 5):
        main()

    else:
        print("\t\t\t\tInvalid input!!")
    goto_menu = input("\t\t\t\tdo you want to go to menu?[y-yes | n-no]: ")
    if (goto_menu == "y" or goto_menu == "Y"):
        main()
    elif (goto_menu == "n" or goto_menu == "N"):
        print("\t\t\t\tInvalid option")


def login(name, password):
    fp = open("login_details.txt","r")
    for i in fp:
        count =0
        us = 0
        ps = 0
        #rs = 0
        for j in i.split():
            if count==2:
                break
            if j == name:
                us = 1
            if j == password:
                ps = 1
            #if j == "R":
                #rs = 1
            count = count + 1
        if us==1 and ps==1:
            print("login success")
        else:
            print("Invalid password or userID")
def new_customer():
    print("\t\t\t\t\t|| New customer ||")
    print('''\t\t\t\t\t1. Create account
    \t\t\t\t2. Loan details 
    \t\t\t\t3. Loan calculator
    \t\t\t\t4. Exit
    ''')
    option = int(input("\t\t\t\tSelect you option:"))
    if(option == 1):
        creat_account()
    elif(option == 2):
        loan_details()
    elif(option == 3):
        loan_calculaotr()
    elif(option == 4):
        main()
    else:
        print("\t\t\t\tinvalid input!!")
        exit(1)


def loan_details():
    print('''\t\t\t\t\t1. We are providing personal loan at only 7% interest rate
    \t\t\t\t2. We are providing car loan at only 11% interest rate
    \t\t\t\t3. We are providing house loan at only 11% interest rate
    \t\t\t\t4. We are providing education loan at only 7% interest rate
    ''')
    goto_menu = input("\t\t\t\tdo you want to go to menu?[y-yes | n-no]: ")
    if(goto_menu == "y" or goto_menu == "Y"):
      main()
    elif(goto_menu == "n" or goto_menu == "N"):
        print("\t\t\t\tInvalid option")

def admin_menu():
    print("\n\t\t\t\t\t\t\t\tMENU")
    print('''\t\t\t\t\t1.Customer's registration request
    \t\t\t\t2.View all transactions
    \t\t\t\t3.View all transactions of specific loan type
    \t\t\t\t4.View all transactions of specific customer
    \t\t\t\t5.View all transaction of all types loan
    \t\t\t\t6.Exit''')
    option = int(input("\n\n\t\t\t\tSelect your option: "))
    if (option == 1):
        print("\t\t\t\tSystem is undergoing maintainance!")
    elif(option == 6):
        main()

def admin():
    admin_login()


def admin_login():
    print("\n\t\t\t\t\t\t\t\t|| ADMIN ||")
    username_admin = input("\n\t\t\t\tUsername: ")
    password_admin = input("\n\t\t\t\tPassword: ")
    password = "Admin#@$117"
    username = "Admin@321"
    if(username == username_admin and password_admin == password):
        print("\t\t\t\tsuccessfully login!!\n\n")
        admin_menu()
    else:
        print("\t\t\t\tusername or password wrong!!")


def creat_account():
    details = []
    name = input("\t\t\t\tFull name: ")
    details.append(name)
    gender = input("\t\t\t\tGender: ")
    details.append(gender)
    dob = input("\t\t\t\tDate of Birth(dd/mm/yy): ")
    details.append(dob)
    address = input("\t\t\t\tAddress: ")
    details.append(address)
    mail = input("\t\t\t\tEmail: ")
    details.append(mail)
    contact = input("\t\t\t\tcontact: ")
    details.append(contact)
    lone_type = input("\t\t\t\tLoan Type: ")
    details.append(lone_type)
    lone_term = input("\t\t\t\tLoan Terms(In years): ")
    details.append(lone_term)
    inst_amount = input("\t\t\t\tInstalment Amount: ")
    details.append(inst_amount)
    id = input("\t\t\t\tUser ID: ")
    details.append(id)

    while 1:
        password = input("\t\t\t\tPassword: ")
        r_password = input("\t\t\t\tRetype Password: ")

        if(password == r_password):
            details.append(password)
            print("\n\n\t\t\t\tAccount created successfully!")
            break
        else:
            print("\t\t\t\twrong password try again!")
            break

    fn = open("costumer details.txt","a")
    for i in range(len(details)):
        fn.write(details[i] + " ")
    fn.write("\n")

    goto_menu = input("\t\t\t\tdo you want to go to menu?[y-yes | n-no]: ")
    if (goto_menu == "y" or goto_menu == "Y"):
        main()
    elif (goto_menu == "n" or goto_menu == "N"):
        exit(1)



def main():
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t|| Welcome to Malaysia Bank ||\n\n\n")
    os.system("cls")
    print('''\t\t\t\t1. Admin
     \t\t\t\t2. New Costumer
     \t\t\t\t3. Registered Costumer
     \t\t\t\t4. Exit''')
    option = int(input("\n\t\t\t\tSelect your option: "))

    if(option == 2):
        opt = new_customer()

    elif(option == 1):
        admin()
    elif(option == 4):
        return
    elif(option == 3):
        # login("nirajan","nirajan22")
        creat_account()
    else:
        print("Invalid option!!")
        return
def changeStatus(name):
    fin = open("studentdetails.txt", "rt")
    data = ""
    for i in fin:
        check = False
        for j in i.split():
            if j == name:
                data = i
                check = True
        if check== True:
            break
    if(data.replace("NR","R")):
        print("User approved by admin")
    else:
        print("user is already approved by admin")
    fin.close()

login("1001","hello")

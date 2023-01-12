import main_file as mf

def newCustomerMenu():
    # print(__name__)
    print("1. Check Loan details.")
    print("2. Loan calculator")
    print("3. Sign Up")
    print("4. Exit")
    choose = int(input("Choose option: "))

    if(choose == 1):
        loanDetails()
    elif(choose == 2):
        loanCalculator()
    elif(choose == 3):
        mf.signUp()
    elif(choose == 4):
        mf.MainMenu()
    else:
        print("Invalid option, Please try again!")
        newCustomerMenu()

def loanDetails():
    print('''\t\t\t\t\t1. We are providing personal loan at only 7% interest rate
        \t\t\t\t2. We are providing car loan at only 11% interest rate
        \t\t\t\t3. We are providing house loan at only 11% interest rate
        \t\t\t\t4. We are providing education loan at only 7% interest rate
        ''')
    # goto_menu = int(input("\n\t\t\t\tPress any key to go to MainMenu: "))
    input("Press any key to continue\n\n")

    mf.MainMenu()

def loanCalculator():
    print('''\t\t\t\t.........Types of loan...........
        \t\t\t\t1. Education Loan (EL)
        \t\t\t\t2. Car Loan (CL)
        \t\t\t\t3. Home Loan (HL)
        \t\t\t\t4. Personal Loan (PL)
        \t\t\t\t5. Exit''')
    option = int(input("\t\t\t\tSelect your loan type: "))
    if (option == 1):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(7)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * (time/12) * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 2):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(11)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * (time/12) * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)


    elif (option == 3):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(11)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * (time/12) * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 4):
        principal = int(input("\t\t\t\tPrincipal: "))
        rate = int(7)
        time = int(input("\t\t\t\tTime(in month): "))
        simple_interes = (principal * (time/12) * rate) / 100
        print("\t\t\t\tinterest = ", simple_interes)

    elif (option == 5):
        mf.MainMenu()
if __name__ == '__main__':
    newCustomerMenu()
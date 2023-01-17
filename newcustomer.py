import main_file as mf

def newCustomerMenu():
    print("\n")
    print("\t-----------------------")
    print("\t|| NEW CUSTOMER MENU ||")
    print("\t-----------------------")
    print("\n")
    print("\t1. Check Loan details.")
    print("\t2. Loan calculator")
    print("\t3. Sign Up")
    print("\t4. Exit\n")
    choose = int(input("\tChoose option: "))
    mf.clear()

    if choose == 1:
        loanDetails()
    elif choose == 2:
        loanCalculator()
    elif choose == 3:
        mf.signUp()
    elif choose == 4:
        mf.MainMenu()
    else:
        print("\n\tInvalid option, Please try again!")
        input("\tPress any key to continue...")
        newCustomerMenu()

def loanDetails():
    print('\n')
    print("\t------------------")
    print("\t|| LOAN DETAILS ||")
    print("\t------------------\n")
    print('''\t1. We are providing personal loan at only 7% interest rate
        2. We are providing car loan at only 11% interest rate
        3. We are providing house loan at only 11% interest rate
        4. We are providing education loan at only 7% interest rate
        ''')
    # goto_menu = int(input("\n\t\t\t\tPress any key to go to MainMenu: "))
    input("\tPress any key to continue...")
    mf.clear()
    mf.MainMenu()

def loanCalculator():
    print("\n\t---------------------")
    print("\t|| LOAN CALCULATOR ||")
    print("\t---------------------\n")
    print('''\t.....Types of loan.....\n
    \t1. Education Loan (EL)
    \t2. Car Loan (CL)
    \t3. Home Loan (HL)
    \t4. Personal Loan (PL)
    \t5. Exit\n''')
    option = int(input("\tSelect your loan type: "))
    if (option == 1):
        principal = int(input("\tPrincipal: "))
        rate = int(7)
        time = int(input("\tTime(in month): "))
        simple_interes = (principal * (time/12) * rate) / 100
        print("\tinterest = ", simple_interes)
        print('\n')
        input('\tPress any key to continue...')
        mf.clear()
        newCustomerMenu()

    elif (option == 2):
        principal = int(input("\tPrincipal: "))
        rate = int(11)
        time = int(input("\tTime(in month): "))
        simple_interes = (principal * (time / 12) * rate) / 100
        print("\tinterest = ", simple_interes)
        print('\n')
        input('\tPress any key to continue...')
        mf.clear()
        newCustomerMenu()

    elif (option == 3):
        principal = int(input("\tPrincipal: "))
        rate = int(11)
        time = int(input("\tTime(in month): "))
        simple_interes = (principal * (time / 12) * rate) / 100
        print("\tinterest = ", simple_interes)
        print('\n')
        input('\tPress any key to continue...')
        mf.clear()
        newCustomerMenu()

    elif (option == 4):
        principal = int(input("\tPrincipal: "))
        rate = int(7)
        time = int(input("\tTime(in month): "))
        simple_interes = (principal * (time / 12) * rate) / 100
        print("\tinterest = ", simple_interes)
        print('\n')
        input('\tPress any key to continue...')
        mf.clear()
        newCustomerMenu()

    elif (option == 5):
        mf.MainMenu()

    else:
        print("\twrong input, try again...\n")
        input("\tpress any key to continue...")
        mf.clear()
        newCustomerMenu()

def newCustomerMenu():
    print("1. Check Loan details.")
    print("2. Loan calculator")
    print("3. Sign Up")
    print("4. Exit")
    choose = int(input("Choose option: "))

    if(choose == 1):
        pass
    elif(choose == 2):
        pass
    elif(choose == 3):
        # signUp()
        pass
    elif(choose == 4):
        exit()
    else:
        print("Invalid option, Please try again!")
        newCustomerMenu()

def loanDetails():
    pass

def loanCalculator():
    pass
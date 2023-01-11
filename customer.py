import main_file as mf
import datetime
import admin as ad
def customerMenu(uid):
    print("1. Loan Details")
    print("2. View Transaction")
    print("3. Pay loan instalment")
    print("4. Loan status")
    print("5. Apply for loan")
    print("6. Exit")

    choose = int(input("Choose option: "))
    if(choose == 1):
        pass
    elif(choose == 2):
        pass
    elif (choose == 3):
        pass
    elif (choose == 4):
        pass
    elif (choose == 5):
        applyLoan(uid)
    elif (choose == 6):
        mf.MainMenu()
    else:
        print("Invalid Input! Try again..")

def applyLoan(id):
    loantype = input("Enter Loan type(EL/CL/HL/PL): ")
    amount = input("Enter Loan amount: ")
    period = input("Time: ")
    loanData = ad.calculateLoan(amount, loantype, period)
    date = datetime.date.today().strftime('%d %b %Y')
    UID = id
    total_amount = int(amount)+int(loanData)
    user = [str(UID),loantype,period,date,amount,str(loanData),str(total_amount)]
    with open('loan_request.txt','a') as file:
        for item in user:
            if(item == user[len(user)-1]):
                file.write(item + ',')
                file.write('\n')
            else:
                file.write(item + ',')
        print('\n')
        print("Your loan request has been submitted, wait for loan approval")

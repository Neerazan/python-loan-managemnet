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
        with open('loan.txt', 'r') as fp:
            for value in fp:
                list_value = value.split(',')
                if uid in list_value:
                    heading = ['LOAN ID', 'USER ID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT', 'TOTAL AMOUNT', 'MONTHLY EMI', 'REMAINING AMOUNT']
                    for i in heading:
                        if (i == heading[len(heading) - 1]):
                            print(i.center(20))
                            print('\t-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                        else:
                            print(i.center(20), end="")

                    for data in list_value:
                        if(data == list_value[len(list_value)-1]):
                            print(data)
                            return
                        else:
                            print(data.center(20), end="")
            print("Sorry, You haven't any loan details until now")
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
    period = input("Time(In months): ")
    # loanData = ad.calculateLoan(amount, loantype, period)
    date = datetime.date.today().strftime('%d %b %Y')
    UID = id
    # total_amount = int(amount)+int(loanData)
    user = [str(UID),loantype,period,date,amount]
    with open('loan_request.txt','a') as file:
        for item in user:
            if(item == user[len(user)-1]):
                file.write(item + ',')
                file.write('\n')
            else:
                file.write(item + ',')
        print('\n')
        print("Your loan request has been submitted, wait for loan approval")

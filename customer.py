import main_file as mf
from datetime import datetime
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
        customerLoanDetails(uid)
    elif(choose == 2):
        pass
    elif (choose == 3):
        makeTransaction(uid)
    elif (choose == 4):
        customerLoanDetails(uid)
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
        print("Your loan request has been submitted, wait for approval")

def transaction(uid):
    print("/t/t/t/t/t/tYOUR LOAN DETAILS")
    print("\n")
    customerLoanDetails(uid)
    print("\n")
    print("/t/t/t/t/tMAKE PAYMENT")
    makeTransaction(uid)

def makeTransaction(uid):
    customerLoanDetails(uid)
    payment = int(input("AMOUNT: "))
    with open('sample.txt', 'r') as fp:
        for value in fp:
            list_value = value.split(',')
            if uid in list_value:
                if (payment < int(list_value[-3]) and int(list_value[-2]) > payment):
                    print(f"You have yo pay minimum of {list_value[-3]}.")
                    makeTransaction(uid)
                elif (payment > int(list_value[-2])):
                    print(f"You have to pay only {list_value[-2]}")
                    makeTransaction(uid)
                elif (payment < int(list_value[-2]) or payment > int(list_value[-2])):
                    updateAmount(uid, payment)
                    return
                else:
                    print("Invalid Input, Try again....")
                    makeTransaction(uid)



def updateAmount(uid, payment):
    with open('sample.txt', 'r') as fp:
        file = fp.readlines()
        print(file)
        print("I'm in updateamount")
        print(uid)
        num = 0
        for value in file:
            num = num + 1
            list_value = value.split(',')
            # print(list_value)
            if (uid in list_value):
                newTotalAmount = int(list_value[-2]) - payment
                updateMonth = int(list_value[3]) - 1
                if ((updateMonth == 0 and newTotalAmount == 0) or newTotalAmount == 0):
                    print("Congratulations, You have paid all the loan...")
                    input("Press any key to continue.....")
                    del file[num - 1]
                    with open('sample.txt', 'w') as f:
                        f.writelines(file)
                        storeTransaction(list_value, str(newTotalAmount), str(payment))
                        return
                list_value[3] = str(updateMonth)
                list_value[-2] = str(newTotalAmount)
                string_value = ','.join([str(elem) for elem in list_value])
                # print(string_value)
                # print(num)
                file[num - 1] = string_value
                with open('sample.txt', 'w') as fn:
                    fn.writelines(file)
                    storeTransaction(list_value, str(newTotalAmount), str(payment))
                    return


def transactionIdGenerator():
    with open('transaction.txt', 'r') as file:
        data_db = file.readlines()
        if(data_db == []):
            return 1
        else:
            value = data_db[-1].split(',')
            UID = value[0]
            return int(UID)+1

def storeTransaction(listData, amount, payment):
    currentDateAndTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    tranctionData = [str(transactionIdGenerator()), listData[0], listData[1], listData[2], currentDateAndTime, payment, amount]
    with open('transaction.txt', 'a') as fp:
        for value in tranctionData:
            if(value == tranctionData[-1]):
                fp.write(value + ',' + '\n')
            else:
                fp.write(value + ',')

def customerLoanDetails(uid):
    with open('sample.txt', 'r') as fp:
        for value in fp:
            list_value = value.split(',')
            if uid in list_value:
                heading = ['LOAN ID', 'USER ID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT', 'TOTAL AMOUNT', 'MONTHLY EMI',
                           'REMAINING AMOUNT']
                for i in heading:
                    if (i == heading[len(heading) - 1]):
                        print(i.center(20))
                        print(
                            '\t-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    else:
                        print(i.center(20), end="")

                for data in list_value:
                    if (data == list_value[len(list_value) - 1]):
                        print(data)
                        return
                    else:
                        print(data.center(20), end="")
        print("Sorry, You haven't any loan details until now")
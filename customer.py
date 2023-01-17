import main_file as mf
from datetime import datetime
# import admin as ad
def customerMenu(uid):
    print("\n")
    print("\t-----------------------")
    print("\t||   CUSTOMER MENU   ||")
    print("\t-----------------------\n")
    print("\t1. Loan Details")
    print("\t2. View Transaction")
    print("\t3. Pay loan instalment")
    print("\t4. Apply for loan")
    print("\t5. Exit")

    choose = int(input("\n\tChoose option: "))
    if(choose == 1):
        mf.clear()
        customerLoanDetails(uid)
    elif(choose == 2):
        mf.clear()
        show_transaction(uid)
    elif (choose == 3):
        mf.clear()
        makeTransaction(uid)
    elif (choose == 4):
        mf.clear()
        applyLoan(uid)
    elif (choose == 5):
        mf.clear()
        mf.MainMenu()
    else:
        print("\tInvalid Input! Try again..")
        input("\n\tPress any key to continue..")
        mf.clear()
        customerMenu(uid)

def applyLoan(id):
    print("\n")
    print("\t--------------------")
    print("\t||   APPLY LOAN   ||")
    print("\t--------------------\n")
    loantype = input("\tEnter Loan type(EL/CL/HL/PL): ")
    amount = input("\tEnter Loan amount: ")
    period = input("\tTime(In months): ")
    # loanData = ad.calculateLoan(amount, loantype, period)
    date = datetime.today().strftime('%d %b %Y')
    # total_amount = int(amount)+int(loanData)
    user = [str(id),loantype,period,date,amount]
    with open('loan_request.txt','a') as file:
        for item in user:
            if(item == user[len(user)-1]):
                file.write(item + ',')
                file.write('\n')
            else:
                file.write(item + ',')
        print('\n')
        print("\tYour loan request has been submitted, wait for approval")
        input("\n\tPress Enter to continue..")
        customerMenu(id)



def makeTransaction(uid):
    print("\n")
    print("\t----------------------")
    print("\t||   MAKE PAYMENT   ||")
    print("\t----------------------\n")
    payment = int(input("\tAMOUNT: "))
    with open('loan.txt', 'r') as fp:
        for value in fp:
            list_value = value.split(',')
            if uid in list_value:
                if (payment < int(list_value[-3]) and int(list_value[-2]) > payment):
                    print(f"\tYou have yo pay minimum of {list_value[-3]}.")
                    input("\n\tPress Enter to continue..")
                    mf.clear()
                    makeTransaction(uid)
                elif (payment > int(list_value[-2])):
                    print(f"\tYou have to pay only {list_value[-2]}")
                    input("\n\tPress Enter to continue..")
                    mf.clear()
                    makeTransaction(uid)
                elif (payment <= int(list_value[-2])):
                    updateAmount(uid, payment)
                else:
                    print("\tInvalid Input, Try again....")
                    input("\n\tPress Enter to continue..")
                    mf.clear()
                    makeTransaction(uid)


def updateAmount(uid, payment):
    with open('loan.txt', 'r') as fp:
        file = fp.readlines()
        num = 0
        for value in file:
            num = num + 1
            list_value = value.split(',')
            # print(list_value)
            if (uid in list_value):
                newTotalAmount = int(list_value[-2]) - payment
                updateMonth = int(list_value[3]) - 1
                if ((updateMonth == 0 and newTotalAmount == 0) or newTotalAmount == 0):
                    print("\n\tCongratulations, You have paid all the loan...")
                    input("\tPress any key to continue.....")
                    del file[num - 1]
                    with open('loan.txt', 'w') as f:
                        f.writelines(file)
                        storeTransaction(list_value, str(newTotalAmount), str(payment))
                        return
                list_value[3] = str(updateMonth)
                list_value[-2] = str(newTotalAmount)
                string_value = ','.join([str(elem) for elem in list_value])
                # print(string_value)
                # print(num)
                file[num - 1] = string_value
                with open('loan.txt', 'w') as fn:
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
    print('\n')
    print("\t\t\t\t\t\t\t\t\t\t----------------------")
    print("\t\t\t\t\t\t\t\t\t\t||   LOAN DETAILS   ||")
    print("\t\t\t\t\t\t\t\t\t\t----------------------\n\n")
    with open('loan.txt', 'r') as fp:
        file_data = fp.readlines()
        line_number = len(file_data)
        count = 0
        new_list = []
        for data in file_data:
            count = count + 1
            list_data = data.split(',')
            if uid in list_data:
                new_list.append(list_data)
            if count == line_number and new_list != []:
                heading = ['LOAN ID', 'USER ID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT', 'TOTAL AMOUNT', 'MONTHLY EMI', 'REMAINING AMOUNT']
                for i in heading:
                    if i == heading[len(heading) - 1]:
                        print(i.center(20))
                        print('    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    else:
                        print(i.center(20), end="")
                for value in new_list:
                    for new_data in value:
                        if new_data == value[len(value) - 1]:
                            print(new_data)

                        else:
                            print(new_data.center(20), end="")
                input("\n\tEnter any key to continue..")
                mf.clear()
                customerMenu(uid)
            if line_number == count and new_list == []:
                print("\tSorry no data found.")
                input("\n\tPrint any key to continue...")
                customerMenu(uid)


def show_transaction(uid):
    print('\n')
    print("\t\t\t\t\t\t\t\t\t\t----------------------")
    print("\t\t\t\t\t\t\t\t\t\t||   TRANSACTION   ||")
    print("\t\t\t\t\t\t\t\t\t\t----------------------\n\n")
    with open('transaction.txt', 'r') as file:
        file_data = file.readlines()
        line_number = len(file_data)
        count = 0
        new_list = []
        for data in file_data:
            count = count + 1
            list_data = data.split(',')
            if uid in list_data:
                new_list.append(list_data)
            if count == line_number and new_list != []:
                heading = ['TRANSACTION ID', 'LOAN ID', 'USER ID', 'LOAN TYPE', 'DATE AND TIME', 'PAYMENT',
                           'REMAINING AMOUNT']
                for i in heading:
                    if i == heading[len(heading) - 1]:
                        print(i.center(20))
                        print('---------------------------------------------------------------------------------------------------------------------------------------------')
                    else:
                        print(i.center(20), end="")

                for value in new_list:
                    for new_data in value:
                        if (new_data == value[len(value) - 1]):
                            print(new_data)

                        else:
                            print(new_data.center(20), end="")
                input("\n\tPress Enter to continue..")
                mf.clear()
                customerMenu(uid)

            if line_number == count and new_list == []:
                print("\n\tNo data found")
                input("\tPress Enter to continue..")
                mf.clear()
                customerMenu(uid)

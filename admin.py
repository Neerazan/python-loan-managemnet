import main_file as mf
# import newcustomer as ns

def customerDetails():
    with open("signup.txt","r") as fp:
        heading = ['UID','NAME','EMAIL','CONTACT','ADDRESS','GENDER','DOB']
        for i in heading:
            if(i == heading[len(heading)-1]):
                print(i.ljust(20))
            # elif(i == heading[2]):
            #     print(i.ljust(30), end="")
            else:
                print(i.ljust(20), end="")
        print("----------------------------------------------------------------------------------------------------------------------------")
        while True:
            data_db = fp.readline()
            if(data_db == ''):
                break
            else:
                data_list = data_db.split(',')
                for value in data_list:
                    # print(value.ljust(20),end='')
                    if(value == data_list[len(data_list) - 1] or value == data_list[len(data_list) - 2]):
                        print("")

                    else:
                        print(value.ljust(20), end="")


def displaLoanRequest():
    print("    .......................................Loan request........................................\n")
    with open("loan_request.txt",'r') as fp:
        heading = ['UID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT']
        for i in heading:
            if (i == heading[len(heading) - 1]):
                print(i.center(20))
            else:
                print(i.center(20), end="")
        print('\t-------------------------------------------------------------------------------------------')
        for data_db in fp:
            list_data = data_db.split(',')
            for data in list_data:
                if (data == list_data[len(list_data) - 1]):
                    print(data.center(20))
                else:
                    print(data.center(20), end="")
    acceptLoan()



def acceptLoan():
    print("\nApprove Loan using respective user ID\n")
    cust_ID = input("Enter customer id: ")
    with open("loan_request.txt","r") as file:
        for value in file:
            ldata = value.split(',')
            if cust_ID in ldata:
                loanType = ldata[1]
                amount = ldata[len(ldata) - 2]
                period = ldata[2]
                loanData = calculateLoan(amount, loanType, period)
                totalPayableAmont = int(amount) + int(loanData)
                monthlyEmi = int(int(totalPayableAmont)/int(period))
                remainingAmount = totalPayableAmont
                loanID = str(generateLoanID())
                ldata.insert(0, loanID)
                ldata.insert(6, str(totalPayableAmont))
                ldata.insert(7, str(monthlyEmi))
                ldata.insert(8, str(remainingAmount))
                with open('loan.txt', 'a') as fl:
                    for i in ldata:
                        if(i == ldata[len(ldata) - 1]):
                            fl.write(i)
                        else:
                            fl.write(i + ',')

#delete user data from loan request file after approving loan
    with open("loan_request.txt","r") as f:
        lines = f.readlines()
        num = 0
        for i in lines:
            num = num + 1
            if(i.split(',')[0] == cust_ID):
                del lines[num -1]

                with open("loan_request.txt","w") as file:
                    for line in lines:
                        file.write(line)


def generateLoanID():
    with open('loan.txt', 'r') as file:
        data_db = file.readlines()
        if(data_db == []):
            return 1
        else:
            value = data_db[-1].split(',')
            UID = value[0]
            return int(UID)+1


def calculateLoan(amount, loanType, Time):
    if(loanType == "EL" or loanType == "el"):
        rate = 15
        simpleInterest = (int(amount) * (int(Time)/12) * rate)/100
        return int(simpleInterest)
    elif(loanType == "CL" or loanType == "cl"):
        rate = 11
        simpleInterest = (int(amount) * (int(Time)/12) * rate) / 100
        return int(simpleInterest)
    elif (loanType == "HL" or loanType == "hl"):
        rate = 11
        simpleInterest = (int(amount) * (int(Time)/12) * rate) / 100
        return int(simpleInterest)
    elif (loanType == "PL" or loanType == "pl"):
        rate = 7
        simpleInterest = (int(amount) * (int(Time)/12) * rate) / 100
        return int(simpleInterest)
    else:
        print("Invalid Input")



#display loan details
def displaLoan():
    print("    ......................................................................Loan Details.......................................................................\n")
    with open("loan.txt",'r') as fp:
        heading = ['LOAN ID', 'USER ID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT', 'TOTAL AMOUNT', 'MONTLY EMI', 'REMAINING AMOUNT']
        for i in heading:
            if (i == heading[len(heading) - 1]):
                print(i.center(20))
            else:
                print(i.center(20), end="")
        print('\t---------------------------------------------------------------------------------------------------------------------------------------------------------')
        for data_db in fp:
            list_data = data_db.split(',')
            for data in list_data:
                if (data == list_data[len(list_data) - 1]):
                    print(data.center(20))
                else:
                    print(data.center(20), end="")




def customer_transaction():
    print('Search transaction using customer ID and loan type(EL,PL,CL,HL)')
    uid = input('Enter user id or loan type: ')
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
                        print(
                            '---------------------------------------------------------------------------------------------------------------------------------------------')
                    else:
                        print(i.center(20), end="")

                for value in new_list:
                    for new_data in value:
                        if (new_data == value[len(value) - 1]):
                            print(new_data)

                        else:
                            print(new_data.center(20), end="")

            if line_number == count and new_list == []:
                with open('loan.txt', 'r') as fl:
                    for data1 in fl:
                        list_data1 = data1.split(',')
                        loan_type = ['EL', 'HL', 'PL', 'CL']
                        if uid in list_data1 or uid in loan_type:
                            print("No transaction")
                            input("press any key to continue.....")
                            return mf.adminMenu()
                    print("wrong input")


def show_all_transaction():
    with open('transaction.txt', 'r') as file:
        file_data = file.readlines()
        line_number = len(file_data)
        count = 0
        new_list
if __name__ == '__main__':
    customerDetails()
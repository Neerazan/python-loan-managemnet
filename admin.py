import main_file as mf
import newcustomer as ns

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
    print("................Loan request..............\n")
    with open("loan_request.txt",'r') as fp:
        heading = ['UID', 'LoanType', 'DATE', 'AMOUNT']
        for i in heading:
            if (i == heading[len(heading) - 1]):
                print(i.center(20))
            else:
                print(i.center(20), end="")
        print('\t------------------------------------------------------------------------')
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
                loanID = str(generateLoanID())
                ldata.insert(0,loanID)
                with open('loan.txt','a') as fl:
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
        rate = 7
        simpleInterest = (int(amount) * int(Time) * rate)/100
        return simpleInterest
    elif(loanType == "CL" or loanType == "cl"):
        rate = 11
        simpleInterest = (int(amount) * int(Time) * rate) / 100
        return simpleInterest
    elif (loanType == "HL" or loanType == "hl"):
        rate = 11
        simpleInterest = (int(amount) * int(Time) * rate) / 100
        return simpleInterest
    elif (loanType == "PL" or loanType == "pl"):
        rate = 7
        simpleInterest = (int(amount) * int(Time) * rate) / 100
        return simpleInterest
    else:
        print("Invalid Input")
if __name__ == '__main__':
    customerDetails()
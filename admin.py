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



def approveLoan():
    print("................Loan request..............\n")
    with open("loan_request.txt",'w') as fp:
        for data_db in fp:
            print(data_db)
    print("\nApprove Loan using their respective user ID\n")
    cust_ID = input("Enter customer id ")

def generateLoanID():
    with open('loan.txt', 'r') as file:
        data_db = file.readlines()
        if(data_db == []):
            return 1
        else:
            value = data_db[-1].split(',')
            UID = value[0]
            return int(UID)+1



if __name__ == '__main__':
    customerDetails()
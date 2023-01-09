import main_file as mf
import newcustomer as ns

def approveNewCustomer():
    with open("signup.txt","r") as fp:
        heading = ['UID','NAME','EMAIL','CONTACT','ADDRESS','GENDER','DOB']
        for i in heading:
            if(i == heading[len(heading)-1]):
                print(i.ljust(20))
            else:
                print(i.ljust(20), end="")
        print("----------------------------------------------------------------------------------------------------------------------------")
        while True:
            data_db = fp.readline().split()
            if(data_db == []):
                break
            else:
                for value in data_db:
                    if(value == data_db[len(data_db) - 1]):
                        print("".ljust(20))
                    else:
                        print(value.ljust(20), end="")

    a = input("Enter customer id to approve the account")
if __name__ == '__main__':
    approveNewCustomer()
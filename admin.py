import main_file as mf
import newcustomer as ns

def approveNewCustomer():
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
                    if(value == data_list[len(data_list) - 1]):
                        print("")

                    else:
                        print(value.ljust(20), end="")

    approveCustomer()

def approveCustomer():
    print("\nApprove customer using their respective user ID\n")
    cust_ID = input("Enter customer id ")

if __name__ == '__main__':
    approveNewCustomer()
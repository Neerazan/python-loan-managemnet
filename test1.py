# def customerLogin():
#     with open("signup.txt", "r") as fp:
#         uid = input("UserID: ")
#         password = input("Password: ")
#         while True:
#             data_db = fp.readline().split()
#             if(data_db == []):
#                 break
#             if (uid == data_db[0] and password == data_db[len(data_db) - 1]):
#                 print("Login Successful")
#
#         print("Invalid User ID or Password please try again!!")
#         customerLogin()
# customerLogin()

# heading = ['UID', 'NAME', 'EMAIL', 'CONTACT', 'ADDRESS', 'GENDER', 'DOB']
# for i in heading:
#     if (i == heading[len(heading) - 1]):
#         print(i.ljust(20))
#     else:
#         print(i.ljust(20), end="")
# print("----------------------------------------------------------------------------------------------------------------------------")
# def approveNewCustomer():
#     with open("signup.txt","r") as fp:
#         while True:
#             data_db = fp.readline()
#             print("this is data from file")
#             print(data_db)
#             if(data_db == []):
#                 break
#             else:
#                 for value in data_db:
#                     if(value == data_db[len(data_db) - 1]):
#                         print("".ljust(20))
#                     else:
#                         print(value.ljust(20), end="")
#
#     a = input("Enter customer id to approve the account: ")
#
# approveNewCustomer()

def approveNewCustomer():
    with open("signup.txt","r") as fp:
        while True:
            data_db = fp.readline()
            if(data_db == ''):
                break
            else:
                data_list = data_db.split(',')
                print(data_list[:len(data_list)-2])
        # if(data_db == '[]'):
        #     break
        # else:
        #     for value in data_db:
        #         if(value == data_db[len(data_db) - 1]):
        #             print("".ljust(20))
        #         else:
        #             print(value.ljust(20), end="")

    # a = input("Enter customer id to approve the account: ")

approveNewCustomer()
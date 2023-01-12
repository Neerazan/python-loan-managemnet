import admin as ad
import customer as cu
import main_file as mf
# def customerLogin():
#     with open("signup.txt", "r") as fp:
#         uid = input("UserID: ")
#         password = input("Password: ")
#         while True:
#             data_db = fp.readline()
#             if(data_db == ''):
#                 break
#             else:
#                 data_list = data_db.split(',')
#                 print(data_list[0])
#                 print(data_list[len(data_list)-1])
#                 if ((uid == data_list[0]) & (password == data_list[len(data_list) - 1])):
#                     print("Login Successful\n")
#                     # cu.customerMenu(uid)
# customerLogin()
# def customerLogin():
#     with open('loan_request.txt','r') as fp:
#         for line in fp:
#             print(line)
# customerLogin()
# import datetime
# date = datetime.date.today().strftime('%d %b %Y')
# print(date)
# def generateLoanID():
#     with open('loan_request.txt', 'r') as file:
#         data_db = file.readlines()
#         if(data_db == []):
#             return 1
#         else:
#             return 2
#             # for data in data_db:
#             #     list_data = data.split(',')
#             #     print(list_data)
#
# generateLoanID()

# with open('loan_request.txt', 'r') as file:
#     data_db = file.readlines()
#     if (data_db == []):
#         print("hell")
#     else:
#         value = data_db[-1].split(',')
#         print(value[0])
# def displaLoanRequest():
#     print("................Loan request..............\n")
#     with open("loan_request.txt",'r') as fp:
#         heading = ['UID', 'LoanType', 'DATE', 'AMOUNT']
#         for i in heading:
#             if (i == heading[len(heading) - 1]):
#                 print(i.center(20))
#             else:
#                 print(i.center(20), end="")
#         print('\t------------------------------------------------------------------------')
#         for data_db in fp:
#             list_data = data_db.split(',')
#             for data in list_data:
#                 if (data == list_data[len(list_data) - 1]):
#                     print(data.center(20))
#                 else:
#                     print(data.center(20), end="")
#     acceptLoan()
#
# def acceptLoan():
#     print("\nApprove Loan using respective user ID\n")
#     cust_ID = input("Enter customer id: ")
#     with open("loan_request.txt","r") as file:
#         for value in file:
#             ldata = value.split(',')
#             if cust_ID in ldata:
#                 loanID = str(ad.generateLoanID())
#                 ldata.insert(0,loanID)
#                 with open('loan.txt','a') as fl:
#                     for i in ldata:
#                         if(i == ldata[len(ldata) - 1]):
#                             fl.write(i)
#                         else:
#                             fl.write(i + ',')
#
# #delete user data from loan request file after approving loan
#     with open("loan_request.txt","r") as f:
#         lines = f.readlines()
#         num = 0
#         for i in lines:
#             num = num + 1
#             if(i.split(',')[0] == cust_ID):
#                 del lines[num -1]
#
#                 with open("loan_request.txt","w") as file:
#                     for line in lines:
#                         file.write(line)
# displaLoanRequest()

def customerLogin():
    uid = input("UserID: ")
    password = input("Password: ")
    with open('signup.txt', 'r') as fp:
        data = fp.readlines()
        for i in data:
            data_list = i.split(',')
            if (uid == data_list[0] and password == data_list[len(data_list) - 2]):
                print("login successfully\n")
                input("Press any key to continue.....\n")
                cu.customerMenu(uid)
                return
        print("invalid usrID or password! try again")
        customerLogin()

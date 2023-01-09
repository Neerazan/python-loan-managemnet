
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
def customerLogin():
    with open('signup.txt','r') as fp:
        print(fp)
        # for line in fp:
        #     print(line.split(','))
customerLogin()
# import main_file
# def testfunc():
#     uid = 'PL'
#     with open('transaction.txt', 'r') as file:
#         file_data = file.readlines()
#         line_number = len(file_data)
#         count = 0
#         new_list = []
#         for data in file_data:
#             count = count + 1
#             list_data = data.split(',')
#             if uid in list_data:
#                new_list.append(list_data)
#             if count == line_number and new_list != []:
#                 heading = ['TRANSACTION ID', 'LOAN ID', 'USER ID', 'LOAN TYPE', 'DATE AND TIME', 'PAYMENT',
#                            'REMAINING AMOUNT']
#                 for i in heading:
#                     if i == heading[len(heading) - 1]:
#                         print(i.center(20))
#                         print(
#                             '---------------------------------------------------------------------------------------------------------------------------------------------')
#                     else:
#                         print(i.center(20), end="")
#
#                 for value in new_list:
#                     for new_data in value:
#                         if (new_data == value[len(value) - 1]):
#                             print(new_data)
#
#                         else:
#                             print(new_data.center(20), end="")
#
#
#             if line_number == count and new_list == []:
#                 with open('loan.txt', 'r') as fl:
#                     for data1 in fl:
#                         list_data1 = data1.split(',')
#                         loan_type = ['EL', 'HL', 'PL', 'CL']
#                         if uid in list_data1 or uid in loan_type:
#                             print("No transaction")
#                             input("press any key to continue.....")
#                             return main_file.adminMenu()
#                     print("wrong input")
#
# testfunc()

# import only system from os
with open('transaction.txt', 'r') as file:
    file_data = file.readlines()
    print(len(file_data))
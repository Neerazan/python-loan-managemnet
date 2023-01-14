# def show_transaction(uid):
#     with open('transaction.txt', 'r') as fp:
#         for data in fp:
#             list_data = data.split(',')
#             if uid in list_data:
#                 heading = ['TRANSACTION ID', 'LOAN ID', 'USER ID', 'LOAN TYPE', 'DATE AND TIME', 'PAYMENT', 'REMAINING AMOUNT']
#
#                 for i in heading:
#                     if (i == heading[len(heading) - 1]):
#                         print(i.center(20))
#                         print('--------------------------------------------------------------------------------------------------------------------------------------------')
#                     else:
#                         print(i.center(20), end="")
#
#                 for value in list_data:
#                     if(value == list_data[len(list_data)-1]):
#                         print(value)
#                         return
#                     else:
#                         print(value.center(20), end="")
# show_transaction('1005')
#
# roll = 1004
# with open('transaction.txt', 'r') as fp:
#     if roll in fp:
#         print("error")

    # for data in fp:
    #     list_data = data.split(',')
    #     print(list_data)
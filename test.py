import main_file as mf
# import customer as cu
def show_transaction(uid):
    heading = ['TRANSACTION ID', 'LOAN ID', 'USER ID', 'LOAN TYPE', 'DATE AND TIME', 'PAYMENT', 'REMAINING AMOUNT']
    for i in heading:
        if i == heading[len(heading) - 1]:
            print(i.center(20))
            print('---------------------------------------------------------------------------------------------------------------------------------------------')
        else:
            print(i.center(20), end="")

    if uid == 'ALL' or uid == 'all':
        with open('transaction.txt', 'r') as file:
            for data in file:
                list_data = data.split(',')
                for value in list_data:
                    if (value == list_data[len(list_data) - 1]):
                        print(value)
                    else:
                        print(value.center(20), end="")
    else:
        with open('transaction.txt','r') as fp:
            for data in fp:
                list_data = data.split(',')
                if uid in list_data:
                    for value in list_data:
                        if(value == list_data[len(list_data)-1]):
                            print(value)
                        else:
                            print(value.center(20), end="")

                else:
                    with open('loan.txt', 'r') as fn:
                        for num in fn:
                            new_data = num.split(',')
                            if uid in new_data:
                                print('This customer have not made any transaction..')
                                input("Press any ket to continue......")
                                mf.adminMenu()
                                return
                        print('Wrong Input!, Try again...')

                        return
    mf.adminMenu()
show_transaction('EL')
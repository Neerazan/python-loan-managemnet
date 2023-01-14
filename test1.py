def customerLoanDetails(uid):
    with open('loan.txt', 'r') as fp:
        for value in fp:
            list_value = value.split(',')
            if uid in list_value:
                heading = ['LOAN ID', 'USER ID', 'LOAN TYPE', 'PERIOD', 'DATE', 'AMOUNT', 'TOTAL AMOUNT', 'MONTHLY EMI',
                           'REMAINING AMOUNT']
                for i in heading:
                    if (i == heading[len(heading) - 1]):
                        print(i.center(20))
                        print('\t-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    else:
                        print(i.center(20), end="")

                for data in list_value:
                    if (data == list_value[len(list_value) - 1]):
                        print(data)
                        return
                    else:
                        print(data.center(20), end="")
        print("Sorry, You haven't any loan details until now")
        input("Press any key to go to Menu...")
customerLoanDetails('1008')
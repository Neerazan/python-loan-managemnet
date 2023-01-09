def customerLogin():
    with open("signup.txt", "r") as fp:
        uid = input("UserID: ")
        password = input("Password: ")
        while True:
            data_db = fp.readline().split()
            if(data_db == []):
                break
            if (uid == data_db[0] and password == data_db[len(data_db) - 1]):
                print("Login Successful")

        print("Invalid User ID or Password please try again!!")
        customerLogin()
customerLogin()
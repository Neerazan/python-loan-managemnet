
def idGenerator():
    with open("signup.txt","r") as fp:
        while True:
            content = fp.readline()
            if(content == ''):
                break
            else:
                list_content = content.split("  ")
                uid = list_content[0]
        return int(uid) + 1

c = idGenerator()
print(c)
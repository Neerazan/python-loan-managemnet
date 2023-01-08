# def idGenerator():
#     with open("signup.txt", "r") as f:
#         a = f.read()
#         if(a == ''):
#             print("Hello")
#             return "1"
#
#         else:
#             with open("signup.txt", "r") as f:
#                 num = 0
#                 print(len(f.readline()))
#                 while num < len(f.readline()):
#                     num+=1
#                     line = f.readline()
#                     uid = line[0]
#                     print(uid)
#                     if(line == ''):
#                         break
#             return str(uid)
# idGenerator()

def idGenerator():
    with open("signup.txt","r") as fp:
        while True:
            content = fp.readline()
            list_content = content.split("  ")
            print(list_content)
            if not content:
                break
idGenerator()
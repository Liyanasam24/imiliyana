def register():
    name = input("enter your user name:")
    password = input("enter your password:")
    with open("user.txt","a") as file_1:
        file_1.write(name)
        file_1.write(password)
        print("REGISTRATION SUCCESSFULL")
def login():
    name=input("enter your name:")
    password= input("enter your password:")
    with open("user.txt","r")as file_1:
        line=file_1.readlines()
        for word in line:
            username,user_password= word.strip().split(',')
            if name == username and password == user_password:
                print("login successful")
                return
    print("invalid")
while True:
    print("REGISTER")
    print("LOGIN")
    option=input("enter your option (1/2):")
    if option=='1':
        register()
    elif option=='2':
        login()
    else:
        print("invalid option")











contacts={"6369641944":"aarthi","9003374866":"saras","9345577862":"imi"}
n=input("enter the name:")
for key,value in contacts.items():
    if n==value:
        print(key)


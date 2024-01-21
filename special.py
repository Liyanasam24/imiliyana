string=input("enter the string:")
special=['@','#','%','*','&']
for i in special:
    string=string.replace(i,"")
print(string)
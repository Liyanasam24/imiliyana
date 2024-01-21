rslt=[]
marks=input("Enter marks:").split(",")
for x in marks:
    if int(x)>35:
        rslt.append("pass")
    else:
        rslt.append("fail")
print(rslt)

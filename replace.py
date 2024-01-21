statement=input("enter a string:")
l=len(statement)
if(l<5):
    print("invalid statement")
else:
    to_replace=statement[0:5]
    print(statement.replace(to_replace,"vglug"))


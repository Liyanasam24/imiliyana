n=int(input("how many members:"))
dup=0
contacts={}
for x in range(n):
    value=input("enter name,num:").split(',')
    contacts[value[0]]=value[1]
print(contacts)
a=input("enter a name:")
for key,value in contacts.items():
    if a==value:
        print(key)
        dup=1
if dup==0:
    print("not found")


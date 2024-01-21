a=input("enter a string:")
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
index=25
for i in a:
    for j in list:
        if i==j:
            print(list[list.index(j)+2],end="")


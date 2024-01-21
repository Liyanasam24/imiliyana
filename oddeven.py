num=int(input("enter the value of N:"))
count_even=0
count_odd=0
for x in range(1,num+1):
    if(x%2)==0:
        count_even+=1
    else:
        count_odd+=1
print("no of even numbers",count_even)
print("no of odd numbers",count_odd)

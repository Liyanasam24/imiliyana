num=int(input("enter a number:"))
sum=0
if(num>0):
      for i in range(1,num+1):
        sum=sum+i
      print("sum of numbers",sum)
else:
    print("invalid number")
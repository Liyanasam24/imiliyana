first_number=int(input("please enter first number:"))
second_number=int(input("please enter second number:"))
limit=int(input("number of fibonacci numbers to be print:"))
print(first_number,end="")
print(second_number,end="")
for i in range(limit +1):
    sum= first_number+second_number
    first_number=second_number
    second_number=sum
    print(sum,end="")


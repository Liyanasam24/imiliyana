print(hi)
try:
a=int(input("enter the number: "))
b=int(input("enter the number:"))
c=a/b
except ZeroDivisionError:
print("cannot divide by zero")
except ValueError:
print("")
print("bye")

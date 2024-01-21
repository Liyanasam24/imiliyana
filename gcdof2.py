# funtion to find the GCD of two numbers
def gcd(a,b):
    for i in range (1, min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    print(gcd)
# main function
a=int(input("enter first number:"))
b=int(input("enter second number:"))
gcd(a,b) # function calling

import math
def gcd(a,b):
    return math.gcd(a,b)
num1=int(input("enter first number"))
num2=int(input("enter the second number"))
result=gcd(num1,num2)
print("gcd of",num1,"and",num2,"is",result)

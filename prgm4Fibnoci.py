n=int(input("enter num"))
a=1
b=1
print("fib series")
for i in range(n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

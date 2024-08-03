import math
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if a%2!=0 and b%2!=0 and a!=b:
    a=a+b
    b=a-b
    a=a-b
    print('a=',a)
    print('b=',b)
elif a%2==0 and b%2==0 and a!=b:
    if a>b:
        print(f"{a} is largest")
    else:
        print(f"{b} is largest")
else:
    a=math.factorial(a)
    b=math.factorial(b)
    print("Factorial")

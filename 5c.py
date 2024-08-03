import math
n=int(input("enter n:"))
x=float(input("enter x:"))
sum1=0
sum2=0
for i in range(2,n+3,4):
    sum1-=(x**i/math.factorial(i))
for i in range(4,n+3,4):
    sum2+=(x**i/math.factorial(i))
print(f"cos({x})={1+sum1+sum2}")
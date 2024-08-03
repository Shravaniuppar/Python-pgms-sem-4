import math
n=int(input("Enter n value:"))
x=float(input("Enter x value:"))
sum1=0
sum2=0
for i in range(1,n+3,4):
    sum1+=(x**i/math.factorial(i))
for i in range(3,n+3,4):
    sum2-=(x**i/math.factorial(i))
j=3
print("Sin series=",end=" ")
for i in range(1,n+3,4):
    print(f"+ {x}^{i}/{i}!",end=" ")
    while j<(n+3):
        print(f"- {x}^{j}/{j}!",end=" ")
        j+=4
        break
print(f"\nSum of sin{x} series is {sum1+sum2}")
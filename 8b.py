n=int(input("Enter a number:"))
s1=0
s2=0
for i in range(1,n+1):
    s1+=(1/i)
for i in range(1,n+1):
    s2+=(i**i/i)
print("sum of 1st series",s1)
print("sum of 2nd series",s2)
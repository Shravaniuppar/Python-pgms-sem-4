n=int(input("Enter n:"))
l=[0,1]
for i in range(n):
    l.append(l[i]+l[i+1])
for i in range(n-1):
  print(l[i],'->',end=' ')
print(l[i+1])

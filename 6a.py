n=int(input("Enter n:"))
for i in range(1,n):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("\n")
    for j in range(i,1):
        print(j,end=' ')
    print()
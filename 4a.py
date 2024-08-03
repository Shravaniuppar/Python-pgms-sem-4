n=int(input("Emter n value:"))
for i in range(n+1,0,-1):
    print(i*' ',end="")
    print((n+1-i)*'* ',)
    
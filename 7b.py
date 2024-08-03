n=input("Enter a number to check for duck number:")
f=0
if n.isnumeric():
    if int(n[0])!=0:
        for i in n:
            if int(i)==0:
                f=1
                break
        if f==1:
            print(n,"is a duck number")
        else:
            print(n,"is not a duck number")
    else:
        print("duck number should not start with 0")
else:
    print("Enter valid number")
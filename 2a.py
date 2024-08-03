ch=input("Enter choice:\nA-bitwise operation \nB-arithmetic operation\n")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if ch=='A':
    print("Bitwise operations")
    c=int(input("Enter choice:\n1-Logical AND\n2-Logical OR\n3-Logical EXOR\n"))
    if c==1:
        print("AND operation result=",a&b)
    elif c==2:
        print("OR operation result=",a|b)
    elif c==3:
        print("EXOR operation result=",a^b)
    else:
        print("Invalid choice")
elif ch=='B':
    print("Arithmetic operations")
    c=int(input("Enter choice:\n1-Add\n2-Sub\n3-Mul\n4-Div"))
    if c==1:
        print("Addition result=",a+b)
    elif c==2:
        print("Subtraction result=",a-b)
    elif c==3:
        print("Multiplication result=",a*b)
    elif c==4:
        print("Division result=",a/b)
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
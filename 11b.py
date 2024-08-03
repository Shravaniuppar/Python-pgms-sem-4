n=int(input("Enter the size of stack:"))
stack=[]
while(1):
    ch=int(input("\nEnter your choice\n1-insertion\n2-deletion\n3-display\n4-stack count\n5-stack empty\n6-stack full\n7-destroy and exit\n"))
    if ch==1:
        if len(stack)<n:
            a=int(input("Enter a number:"))
            stack.append(a)
        else:
            print("\nStack is full\n")
    elif ch==2:
        if len(stack)!=0:
            print("\nPopped element:",stack.pop())
        else:
            print("\nStack is empty\n")
    elif ch==3:
        print("\n")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
        print("\n")
    elif ch==4:
        print("\nStack count=",len(stack))
    elif ch==5:
        if len(stack)==0:
            print("\nStack is empty\n")
        else:
            print("\nStack is not empty\n")
    elif ch==6:
        if len(stack)==n:
            print("\nStack is full\n")
        else:
            print("\nStack is not full\n")
    elif ch==7:
        for i in stack:
            stack.pop()
        break
    else:
        print("\ninvalid choice")
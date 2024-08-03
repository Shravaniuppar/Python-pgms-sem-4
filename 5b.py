print("Enter the numbers and press -1 to terminate:")
pr=1
n=int(input())
if n!=-1:
    while(n!=(-1)):
        pr*=n
        n=int(input())
        m=pr
        if n==-1:
            break
    print("Product of all numbers=",pr)
else:
    print("code terminated because 1st number is -1")
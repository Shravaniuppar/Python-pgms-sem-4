n=int(input("Enter a number:"))
if (n%2==0 and n//2==1) or (n%3==0 and n//3==1) or (n%5==0 and n//5==1):
    print('Ugly number')
else:
    print("Not a ugly number")
print("Enter the x and y coordinates of all the three points:")
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
a=0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
if a==0:
    print("Points are collinear")
else:
    print("Points are not collinear")

s=input("Enter a alphanumeric string along with spl cahracters:")
f=0
spc=0
numc=0
if s.isnumeric():
    for i in s:
        numc+=int(i)
    print("Sum of the numerics enterd=",numc)
elif s.isalpha():
    if s.islower():
        print("Alphabets are in lower case")
    else:
        print("Alphabets are in upper case") 
elif s.isalnum():
    print("Entered string is both alphabetic and numeric ")
else:
    for i in s:
        spc+=1
    print("Num of the spl characters enterd=",spc)
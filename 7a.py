s=input("Enter a string:")
v=['a','e','i','o','u']
ct=0
if s.isalpha():
    for i in s:
        if i.lower() not in v:
               ct+=1
    print("Consonant count:",ct)
    if s.startswith('T'):
        print("Letter starts with T")
    else:
        print("Letter does not starts with T")
elif s.isnumeric():
    s1=s[::-1]
    print("Reversed numbers:",s1)

    
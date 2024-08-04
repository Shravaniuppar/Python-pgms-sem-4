import re
s=input("enter a pin code:")
k=r'[1-9]{1}[0-9]{5}|[1-9]{1}[0-9]{2}\s[0-9]{3}'
v=re.findall(k,s)
if v:
    print("valid")
else:
    print("invalid")
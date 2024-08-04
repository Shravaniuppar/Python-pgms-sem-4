import re
s=input("enter a ifsc code:")
k=r"[A-Z]{4}0[a-z A-Z 0-9]{6}"
v=re.findall(k,s)
if v:
    print("valid")
else:
    print("invalid")
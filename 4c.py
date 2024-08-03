from datetime import *
dob=input("enter dob(DD-MM-YYYY):")
print(date.today().year)
yr=date.today().year
age=yr-int(dob[6::])
print("Age:",age)
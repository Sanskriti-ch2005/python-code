gender = str(input("enter the gender:"))
age = int(input("enter the age:"))
status1 = str(input("enter the status(married/ unmarried)"))
if age >= 30 and status1 == "unmarried" and gender == "male":
    print("you are selected for this role", gender)
elif age <= 30 and status1 == "unmarried"and gender == "female":
    print("you are selected for this role:", gender)
else:
    print("you are not matched with carteria")
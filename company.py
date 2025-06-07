male = int(input("enter the age of male candidate:" ))
status1 = str(input("enter the status(married/ unmarried)"))
female = int(input("enter the ange of female candidate:"))
status2 = str(input("enter the status(married/unmarried)"))
if male >= 30 and status1 == "unmarried":
    print("you are selected for this role", male)
if female <= 30 and status2 == "unmarried":
    print("you are selected for this role:", female)
else:
    print("you are not matched with carteria")
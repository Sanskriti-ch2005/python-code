unit = float(input("enter the unit"))
tax = 0.2
total  = unit + tax
if total  <= 50:
    print("price will be 0.50 per unit" , total )
if total  <= 100:
    print("price will be 0.75 per unit", total )
if total  >= 100:
    print("price will be 1.75 per unit", total )
if total  > 250:
    print("price will be 1.5 per unit", total )
else:
    print("the is not match the condition to apply bill")

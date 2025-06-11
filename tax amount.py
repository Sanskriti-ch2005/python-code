# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
balance = float(input("total balance:"))
amount = int(input("withdraw amount:"))
tax = 2.5
print("tax include:", tax)
if amount %5==0:
    total = amount + tax
if tax <= balance:
    remaining = balance-total
    print("total withdraw amount:", total)
    print("remaining amount:", remaining)
else:
    print("Invalid amount, please enter the amount which is multiple of 5")

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
amount = 1870
note500 = amount//500
if amount >= 500:
    amount %= 500
    print("note of 500:", note500)
else:
    print("note500 = 0")
    
if amount >= 200:
    note200 = amount//200
    amount %= 200
    print("note of 200:", note200)
else:
    print("note200 = 0")
    
if amount >= 100:
   note100 = amount//100
   amount %= 100
   print("note of 100:", note100)
else:
   print("note100 = 0")
   
if amount >= 50:
    note50 = amount//50
    amount %= 50
    print("note of 50:", note50)
else:
    print("note50 = 0")
    
if amount >= 20:
    note20 = amount//20
    amount %= 20
    print("note of 20:", note20)
else:
    print("note20 = 0")
    
if amount >= 10:
    note10 = amount//10
    amount %= 10
    print("note of 10:" , note10)
else:
    print("note10 = 0")
row = int(input("enter the number"))
for i in range (1, row+1):
    for j in range((row-1)):print(''*(row-i)+'*'*j)

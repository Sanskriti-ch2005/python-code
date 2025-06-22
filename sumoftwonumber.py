num = int(input("enter the number"))
total = 0
while  num>0:
    digit = num%10
    total += digit
    num = num//10
print("the sum is", total)
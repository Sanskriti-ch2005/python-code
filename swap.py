num = int(input("enter the number"))
last_digit = num%10
first_digit = num
while first_digit >= 10:
    first_digit //= 10
first_digit , last_digit = last_digit , first_digit
print ("first_digit = " ,first_digit)
print("last_digit = " ,last_digit)
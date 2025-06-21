num = int(input("enter the number"))
last_digit = num%10
first_digit = num
while first_digit >= 10:
    first_digit //= 10
sum = last_digit + first_digit
print ("the first num is" ,first_digit)
print("the last num is" ,last_digit)
print("the sum is", sum)
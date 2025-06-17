num = int(input("enter the nnumber"))
i = num
sum = 0
while i > 0:
    last = i % 10
    sum += last ** 3
    i //= 10
if sum == num:
    print("the number is armstrom number")
else:
    print("this is not armstrom number")
    

# num = int(input("enter the number"))
# factorial = 1
# i = 1

# while i<=num :
#     factorial = factorial*i
#     i += 1

# print("the factorial is", factorial)

num = int(input("enter the number"))
fact = 1
i = num
sum = 0
while (num>0):
    last = num%10
    num = int(num/10)
    print(last)
    while(last>0):
        fact *= last
        last -= 1
    sum += fact
    fact = 1

if (sum==i):
    print("this is a strong number",sum)
else:
    print("not a strong number")

# num = int(input("enter the nnumber"))
# i = num
# sum = 0
# while i > 0:
#     last = i % 10
#     sum += last ** 3
#     i //= 10
# if sum == num:
#     print("the number is armstrom number")
# else:
#     print("this is not armstrom number")
    

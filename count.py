num = int(input("inter the number"))
n = num
count=0
while n > 0:
    n = n//10
    count += 1
if num == 0:
    count = 1
print("number of digit", count)

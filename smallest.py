a = int(input("enter the number")) 
b = int(input("enter the number")) 
c = int(input("enter the number")) 
if a <= b and a <= c:
    print("a is smallest number", a)
elif b <= a and b <= c:
    print("b is smallest number", b)
else:
    print("c is smallest number", c)
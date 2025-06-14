row= int(input("enter the row"))
for i in range(1,row+1):
    for j in range(65, 65+i):
        print(chr(j), end='')
    print()
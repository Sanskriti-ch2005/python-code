row= int(input("enter the row"))
for i in range(row):
    for j in range(i+1):
        print(chr(65+i), end='')
    print()
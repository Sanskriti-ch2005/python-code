totalnumber = 600 
physics = int(input("enter the number"))
chemistry = int(input("enter the number"))
biology = int(input("enter the number"))
maths = int(input("enter the number"))
computer = int(input("enter the number"))
total = physics+chemistry+biology+maths+computer 
percentage = ( total/totalnumber)*100 
if percentage >= 90:
    print("Grade A", percentage)
elif percentage >= 80:
    print("Grade B ", percentage)
elif percentage>= 70:
    print("grade C", percentage )
elif percentage >= 60:
    print("Grade D", percentage,)
elif percentage >= 40:
    print("Grade E", percentage)
elif percentage <= 40:
    print("Grade F", percentage)
else:
    print("you are fail")

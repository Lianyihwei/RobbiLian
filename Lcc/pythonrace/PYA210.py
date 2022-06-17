side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

if (side3+side2 >= side1):
    print(side1+side2+side3)
elif side1+side2 >= side3:
    print(side1+side2+side3)
elif (side1+side3 >= side2):
    print(side1+side2+side3)
else:
    print("Invalid")

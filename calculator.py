print("simple calculator")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
print("select operator:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=input("enter your choice(1/2/3/4):")
if choice=='1':
    print("result:",num1+num2)
elif choice=='2':
    print("result:",num1-num2)
elif choice=='3':
    print("result:",num1*num2)
elif choice=='4':
    if num2!=0:
        print("result:",num1/num2)
    else:
        print("Error!Division by Zero")
else:
    print("Invalid Input")

    

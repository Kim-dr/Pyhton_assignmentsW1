#Enter the numbers you want to calculate and the operation you want to perform
num1=(float(input("Enter the first number:")))
num2=(float(input("Enter the second number:")))
operation=input("Enterthe operation (+,-,*,/):")

if operation == "+":
    reult = num1+num2
elif operation== "-":
    result=num1 -num2
elif operation== "*":
    result=num1*num2
elif operation=="/":
    if num2 !=0:
        result=num1/num2
    else:
        result="Error :division by zero is not allowed" 
else:
        result ="Invalid operation : please enter +,-,* or /"

print("The result is:", result)
        
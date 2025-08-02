num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
operation=input("Enter a maths operation here:")

if operation =='+':
    result=num1+num2
    print(f"{num1}+{num2}={result}")

elif operation =='-':
    result=num1-num2
    print(f"{num1}-{num2}={result}")

elif operation =='*':
    result=num1*num2
    print(f"{num1}*{num2}={result}")

elif operation =='/':
    if num2!=0:
        result=num1/num2
        print(f"{num1}/{num2}={result}")

    else:
        print("Error: Division by zero not possible.")
else:
    print("Invalid operation. Please put +,-,*, or /")

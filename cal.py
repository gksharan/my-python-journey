firstno = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
secondno = int(input("Enter the second number: "))

if operation == "+":
    result = firstno + secondno
    print("The result is:", result)
elif operation == "-":
    result = firstno - secondno
    print("The result is:", result)
elif operation == "*":
    result = firstno * secondno
    print("The result is:", result)
elif operation == "/":
    if secondno == 0 :
        print("Error: Division by zero is not allowed.")
    else:
        result = firstno / secondno
        print("The result is:", result)     
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")
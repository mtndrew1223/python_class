def calculator():
    operation = input("Choose an operation (+, -, *, /): ")
    
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation")
        return
    
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input, please enter numeric values.")
        return

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    print(f"The result is: {result}")

calculator()

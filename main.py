def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def get_number(Message):
    while True:
        try:
            return float(input(Message))
        except ValueError:
            print("That is not a valid number. Please try again.")

print("Welcome to the calculator program!")
print("Available Operations: +  -  *  /")

while True:
    num1 = get_number("Enter the first number: ")
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = get_number("Enter the second number: ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation"

    print("Result:", result)

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
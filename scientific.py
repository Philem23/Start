import math

def basic_calculator():
    print("Simple Calculator with Scientific Functions")
    print("Available operations: +, -, *, /, sqrt, pow, sin, cos, exit")

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == 'exit':
            print("Goodbye!")
            break

        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == '+':
                    print(f"Result: {num1 + num2}")
                elif operation == '-':
                    print(f"Result: {num1 - num2}")
                elif operation == '*':
                    print(f"Result: {num1 * num2}")
                elif operation == '/':
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        elif operation == 'sqrt':
            try:
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error: Cannot take square root of negative number.")
                else:
                    print(f"Result: {math.sqrt(num)}")
            except ValueError:
                print("Invalid input.")
        
        elif operation == 'pow':
            try:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {math.pow(base, exponent)}")
            except ValueError:
                print("Invalid input.")

        elif operation == 'sin':
            try:
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {math.sin(math.radians(angle))}")
            except ValueError:
                print("Invalid input.")

        elif operation == 'cos':
            try:
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {math.cos(math.radians(angle))}")
            except ValueError:
                print("Invalid input.")
        
        else:
            print("Unknown operation. Try again.")

if __name__ == "__main__":
    basic_calculator()

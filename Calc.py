while True:

    operation = input('Select operation: sum,difference,multiplication,division: ')

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))

    sum = (num1 + num2)
    difference = (num1 - num2)
    multiplication = num1 * num2
    division = num1 / num2

    if operation.lower() == "sum":
        print(f"The sum is {sum}")
    elif operation.lower() == "difference":
        print(f"The difference is {difference}")
    elif operation.lower() == "multiplication":
        print(f"{num1} * {num2} = {multiplication} ")
    elif operation.lower() == "division":
        print(f"{num1} / {num2} = {division}")

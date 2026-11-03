print("Welcome to My Calculator!")

history = []

while True:
    num1 = float(input("\nEnter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator"

    print("Result:", result)

    history.append(f"{num1} {operator} {num2} = {result}")

    choice = input("\nDo you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nCalculation History:")
for item in history:
    print(item)

print("\nThank you for using my calculator!")

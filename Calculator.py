def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))

        if choice == 5:
            print("Exiting the calculator.")
            break
        elif choice not in (1, 2, 3, 4):
            print("Invalid choice. Please enter a valid option.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            try:
                print("Result:", divide(num1, num2))
            except ValueError as ve:
                print(ve)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
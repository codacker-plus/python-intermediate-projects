def calculator():
    print("\nSimple Calculator in Python 🧮")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        again = input("Do you want to continue? (y/n): ")
        if again.lower() != 'y':
            print("Exiting calculator.\n")
            break

if __name__ == "__main__":
    calculator()

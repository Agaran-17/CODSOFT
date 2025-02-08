def display_menu():
    """Display the calculator menu."""
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentation")
    print("6. Module")
    print("7. Exit")

def get_numbers():
    """Prompt the user to input two numbers."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def add(num1, num2):
    """Perform addition."""
    return num1 + num2

def subtract(num1, num2):
    """Perform subtraction."""
    return num1 - num2

def multiply(num1, num2):
    """Perform multiplication."""
    return num1 * num2

def divide(num1, num2):
    """Perform division."""
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 / num2

def exponentation(num1,num2):
    return num1**num2
def module(num1,num2):
    return num1%num2


def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4","5","6"]:
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {num1} / {num2} = {result}")
        elif choice=="5":
            result=exponentation(num1,num2)
            print(f"result:{num1}**{num2}={result}")
        elif choice==6:
            result=module(num1,num2)
            print(f"result:{num1}%{num2}={result}")

if __name__ == "__main__":
    main()
''' 
Task 1 :Build a Calculator CLI App.
 Objective:  Create a command-line calculator supporting basic operations.
 Tools:  Python, VS Code / any text editor, terminal.
 Deliverables:   A Python script (calculator.py).
 Hints/Mini Guide:
 1.Use functions for each operation (+, -, *, /)
 2.Take user input using input()
 3.Loop until user chooses to exit
 Outcome:   A wel-structured schema.

'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def get_number(nmbr):
    while True:
        try:
            return float(input(nmbr))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def show_menu():
    print("\n====== Simple CLI Calculator ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("===================================")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("❌ Invalid choice! Please choose a valid option (1-5).")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'

        print(f"✅ Result: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()

def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid integer numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print("Division result:", result)
    finally:
        print("Operation complete.")

divide_numbers()

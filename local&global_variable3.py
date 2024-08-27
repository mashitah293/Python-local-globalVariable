def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result
    finally:
        print("Division operation completed.")

# Ask the user to input two numbers
try:
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))

    # Call divide_numbers with the user inputs
    result = divide_numbers(a, b)
    
    # Print the result if the division is successful
    if result is not None:
        print(f"The result of {a} divided by {b} is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")


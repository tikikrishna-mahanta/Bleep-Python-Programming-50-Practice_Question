try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

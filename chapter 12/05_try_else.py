try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The division of {a} and {b} is {a / b}.")
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Division was successful.")
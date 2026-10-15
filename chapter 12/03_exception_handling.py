# a = int(input("Enter a number: "))

# print(a)

try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
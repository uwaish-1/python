import random
n = random.randint(1, 100)

a = int(input("Guess a number between 1 and 100: "))

while a != n:
    if a < n:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    a = int(input("Guess a number between 1 and 100: "))
    
print("Congratulations! You guessed the number.")
'''
1 for snake
-1 for water
0 for gun

'''

import random


you = int(input("Enter 1 for snake, -1 for water, 0 for gun: "))
youDict = {1: "snake", -1: "water", 0: "gun"}
computer = random.choice([-1, 0, 1])
if you == computer:
    print(f"Computer chose {youDict[computer]} and you chose {youDict[you]}. It's a tie!")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print(f"Computer chose {youDict[computer]} and you chose {youDict[you]}. You win!")
else:
    print(f"Computer chose {youDict[computer]} and you chose {youDict[you]}. Computer wins!")

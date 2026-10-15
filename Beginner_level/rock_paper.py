import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

# choices = get_choices()
# print(f"Player choice: {choices['player']}")
# print(f"Computer choice: {choices['computer']}")

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
        
choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)











# food = ["pizza", "hamburger", "hotdog"]
# dinner = random.choice(food)
# print(dinner)
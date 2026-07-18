import random
print("Rock Paper Scissors")
choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()
computer = random.choice(choices)

print("Computer:", computer)

# Tie case
if user == computer:
    print("it's a Tie")

# Your winning cases
elif user == "rock" and computer == "scissors":
    print("you win")

elif user == "paper" and computer == "rock":
    print("you win")

elif user == "scissors" and computer == "paper":
    print("you win")

# Computer winning cases
elif computer == "rock" and user == "scissors":
    print("Computer win")

elif computer == "paper" and user == "rock":
    print("Computer win")

elif computer == "scissors" and user == "paper":
    print("Computer win")

# Invalid input
else:
    print("Invalid input")

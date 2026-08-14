import random
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
user = input("Enter rock, paper, or scissors: ").lower()
if user not in choice:
    print("Invalid input. Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose {computer}.")
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
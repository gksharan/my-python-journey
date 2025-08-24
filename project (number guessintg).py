import random

num = random.randint(1, 100)

while True:
    try:
        user_input = input("Guess a number or type 'exit': ")
        
        # Check for the exit command before trying to convert to an integer
        if user_input.lower() == 'exit':
            print("Exiting the game. The correct number was:", num)
            break
            
        user_guess = int(user_input)
        
        if user_guess < num:
            print("Too low")
        elif user_guess > num:
            print("Too high")
        else: # The only remaining condition is that the guess is correct
            print("You have guessed the correct number!")
            break # Exit the loop after the correct guess

    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
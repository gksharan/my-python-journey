import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct!")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")
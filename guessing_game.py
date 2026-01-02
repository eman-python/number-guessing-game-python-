import random

secret_number = random.randint(1, 20)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
    elif guess < secret_number:
        print("Too low, try a higher number.")
    else:
        print("Too high, try a lower number.")

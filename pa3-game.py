import random
secret_number = random.randint(1, 100)
print("The computer has chosen a number between 1-100, guess the number!")
guess_number = int(input("How many guesses would you like? "))
if guess_number <= 0:
    print("Guess number not valid")
else:
    attempt = int(input("Enter your guess: "))
    while attempt != secret_number:
        guess_number -= 1
        if attempt > secret_number:
            guess = "Guess lower!"
        elif attempt < secret_number:
            guess = "Guess higher!"
        if guess_number > 0:
            attempt = int(input(guess+" You have " + str(guess_number) + " more guesses. Enter your guess: "))
        elif guess_number == 0:
            win_or_lose = 0
            break
        if (attempt == secret_number) and (guess_number > 0):
            win_or_lose = 1
            break
    if win_or_lose == 0:
        print("Better luck next time")
    if win_or_lose == 1:
        print("Great game! You guessed the number!")

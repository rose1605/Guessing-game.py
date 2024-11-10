import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guessing_game()

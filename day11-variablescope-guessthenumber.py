import random

chosen_number = 0


def computeChances(difficulty_level):
    if (difficulty_level == "easy"):
        return 10
    elif (difficulty_level == "hard"):
        return 5
    else:
        return -1


def calculate(guessed_number):
    match = False
    if (guessed_number < chosen_number):
        print("Too low.")
    elif (guessed_number > chosen_number):
        print("Too high.")
    else:
        print(f"You got it! The answer was {chosen_number}")
        match = True
    return match


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chosen_number = random.randint(1, 100)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

number_of_chances = computeChances(difficulty_level)

if (number_of_chances == -1):
    print("Invalid choice, try again!!")
match = False
while (number_of_chances > 0 and not match):
    print(
        f"You have {number_of_chances} attempts remaining to guess the number."
    )
    guessed_number = input("Make a guess: ")
    match = calculate(int(guessed_number))
    number_of_chances -= 1
    if (not match and number_of_chances > 0):
        print("Guess again.")

if (not match):
    print(
        f"You've run out of guesses, you lose. The answer was {chosen_number}")

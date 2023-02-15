# checking matches in strings

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Please guess a letter :: ")
match = 0
for letter in chosen_word:
  if (letter == guess):
    match = 1
if (match == 1):
    print("Right")
else:
    print("Wrong")


#  Display a string with dashes and updated with the user's guess

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for n in range(0, len(chosen_word)):
  display.append("_")
print(f"Display word : {display}")

while ("_" in display):
  guess = input("Guess a letter: ").lower()
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter 
  print(display)


# hangman skelton code

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while (not end_of_game and lives > 0):
    guess = input("Guess a letter: ").lower()
    match = 0
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            match = 1
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    if(match == 0):
      lives -= 1
      print(stages[lives])
      if (lives == 0):
            print("You lose")
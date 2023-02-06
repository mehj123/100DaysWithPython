import random

random_int = random.randint(0,1)
if(random_int == 1):
    print("Heads")
else:
    print("Tails")



# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_int = random.randint(0,len(names)-1)
print(f"{names[random_int]} is going to buy a meal today!")

#lists
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position) // 10
row = int (position) % 10
map[row - 1][col - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


#Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_map = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice_0 = game_map[int(user_choice)]
print(choice_0)
computer_choice = random.randint(0,2)
choice_1 = game_map[computer_choice]
print(f"Computer chose : {choice_1}")

if(choice_0 == 0 and choice_1 == 2):
  print("You WIN!!")
elif(choice_0 < choice_1):
  print("Computer wins!!")
elif(choice_1 < choice_0):
  print("You WIN!!")
elif(choice_0 == choice_1):
  print("DRAW!!")
else:
  print("Wrong choice!!")

  



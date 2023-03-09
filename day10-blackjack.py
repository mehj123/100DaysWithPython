import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    return random.choice(cards)


def sum_cards(cards_list):
    total = sum(cards_list)
    if(total > 21):
      if(11 in cards_list):
        total -= 10
    return total

def check_sum(users_cards_sum, dealers_cards_sum):      
    if (users_cards_sum > 21):
          return "1"
    elif (dealers_cards_sum > 21):
          return "2"
    elif (users_cards_sum == dealers_cards_sum):
          return "3"
    else:
          if (21 - users_cards_sum < 21 - dealers_cards_sum):
              return "1"
          else:
              return "2"

def print_result(result, users_cards, users_cards_sum, dealers_cards, dealers_cards_sum):
  print(f"Your final hand:{users_cards}, final score: {users_cards_sum}")
  print(f"Computer's final hand:{dealers_cards}, final score: {dealers_cards_sum}")
  if(result == "1"):
    print("You Win!!")
  elif(result == "2"):
    print("You Lose!!")
  else:
    print("It is a DRAW!!")

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
users_cards = []
dealers_cards = []
user_first_card = deal_cards()
users_cards.append(user_first_card)
dealers_first_card = deal_cards()
dealers_cards.append(dealers_first_card)

while play_game == 'y':   
    user_next_card = deal_cards()
    users_cards.append(user_next_card)
    dealers_next_card = deal_cards()
    dealers_cards.append(dealers_next_card)

    users_cards_sum = sum_cards(users_cards)
    dealers_cards_sum = sum_cards(dealers_cards)

    result = check_sum(users_cards_sum, dealers_cards_sum)
  
    if(users_cards_sum >= 21) or (dealers_cards_sum >= 21):
      if(users_cards_sum > 21 or dealers_cards_sum == 21):
        result = "2"
        print_result(result, users_cards, users_cards_sum, dealers_cards, dealers_cards_sum )
        play_game = "n"
      if(dealers_cards_sum > 21 or users_cards_sum == 21):
        result = "1"
        print_result(result, users_cards, users_cards_sum, dealers_cards, dealers_cards_sum )
        play_game = "n"
    else:
      print(f"Your cards {users_cards}, current score: {users_cards_sum}")
      print(f"Computer's first card: {dealers_first_card}")
      get_another_card = input("Type 'y' to get another card, type 'n' to pass:")
      if (get_another_card == "n"):         
          result = check_sum(users_cards_sum, dealers_cards_sum)
          print_result(result, users_cards, users_cards_sum, dealers_cards, dealers_cards_sum )
          play_game = "n"
        


from replit import clear

bidding_list = {}


def getbids():
    clear()
    bid_name = input("What is your name?: ")
    bid_value = input("What is your bid? $")
    bidding_list[bid_name] = bid_value


def calculatebids():
    winning_bid = 0
    winning_name = ""
    for name in bidding_list:
        current_bid = int(bidding_list[name])
        if (current_bid >= winning_bid):
            winning_name = name
            winning_bid = current_bid
    print(f"The winner is {winning_name} with a bid of ${winning_bid}")


more_players = "yes"
while (more_players == 'yes'):
    getbids()
    more_players = input("Are there any more bidders? Type 'yes' or 'no'.")
    if (more_players != 'yes'):
        clear()
        calculatebids()

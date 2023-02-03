print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

count_for_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

count_for_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

total_count = int(str(count_for_true) + str(count_for_love))

if( total_count < 10 or total_count > 90 ):
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif( total_count >= 40 and total_count <= 50 ):
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
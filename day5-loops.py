# Average height without using sum()

student_heights = input("Input a list of student heights ").split()
no_of_students = len(student_heights)
sum_of_height = 0
for n in range(0, no_of_students):
  sum_of_height+=int(student_heights[n])
average = round(sum_of_height / no_of_students)
print(average)


# Maximum score without using max()
student_scores = input("Input a list of student scores ").split()
max_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if(max_score <= student_scores[n]):
        max_score = int(student_scores[n])
print(student_scores)
print(f"The highest score in the class is: {max_score}")


# Sum of even numbers upto 100
total = 0
for even_number in range(2,101,2):
    total += even_number
print(total)

# Fizz buzz game
for number in range(1,101):
    if((number % 3 == 0) and (number % 5 == 0)):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for letter in range(0,nr_letters):
  password.append(letters[letter])
for symbol in range(0,nr_symbols):
  password.append(symbols[symbol])
for number in range(0,nr_numbers):
  password.append(numbers[number])
print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for letter in range(0,nr_letters):
  password.append(random.choice(letters[letter]))
for symbol in range(0,nr_symbols):
  password.append(random.choice(symbols[symbol]))
for number in range(0,nr_numbers):
  password.append(random.choice(numbers[number]))
print(password)
random.shuffle(password)
print(password)
pass_word=""
for char in password:
  pass_word+= char
print(pass_word)
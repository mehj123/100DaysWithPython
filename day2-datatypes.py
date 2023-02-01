#Data Types
#String
print("Hello")
#Integer
print(123 + 345)
#Large Integers -> can use _ to show ,
print(123_456_789)
#Float
print(100.89)
#Boolean - > True and False
#check the type of data
num_char = 6
print(type(num_char))
#type checking / type conversion
#convert to str
new_num_char = str(num_char)
print(type(new_num_char))

#Adding the digits in the input
two_digit_number = input("Type a two digit number: ")
print(str(int(two_digit_number[0]) + int(two_digit_number[1])))

#Mathematical operator
# Addition - > 3 + 5
# Subtraction -> 7 -4
# Multiply -> 3 * 2
# Divide - > 6/3 -> always returns a float e.g (2.0)
# exponent - > 2 ** 3
print(2 ** 3) # returns 8
# round
print(round(8/3))
print(round(8/3, 2)) # 2 is the decimal precision
# Floor -> //
print(6 // 3) # returns a whole number instead of float

# F String - formatting without type conversion
score = 0
height = 1.5
winning = True
print(f"your score is {score}, your height is {height}, winning is {winning}")

#bmi calculator
#bmi = weight/height squared

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)
print(int(bmi))

#Life in weeks
age = input("What is your current age? ")
years_left = 90 - int(age)
days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")





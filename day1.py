# Print
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Single print statement with multiple lines
print("\nDay 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# input from console, then print
print("Hello " + input("Enter your name \n"))

# print length of name input from console
# str -  for converting length to string for concatenation - otherwise returns TypeError: can only concatenate str (not “int”) to str
print("Length of your name " + str(len(input("What is your name? "))))

# Variables
name = input("Enter your name \n")
print("Your name is : " + name)

# variable naming conventions
# 1. multiple names should be separated by "_" e.g user_name
# 2. should not start with numbers but can contain numbers e.g. length1
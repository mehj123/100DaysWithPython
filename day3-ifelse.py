#BMI 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
rounded_bmi = round(bmi)
if rounded_bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif rounded_bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif (rounded_bmi > 25 and rounded_bmi < 30):
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif rounded_bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")




# Leap year check
year = int(input("Which year do you want to check? "))
leap_year = False
if(year % 4 == 0):
    leap_year = True
elif( year % 100 != 0 and year % 400 == 0):
    leap_year = True
if(leap_year != True):
    print("Not leap year.")
else:
    print("Leap year.")
# Define the following variables
# name, last_name, species, eye_color, hair_color, age
# name = 'Lana'
import datetime
# Prompt user for input and Re-assign these
name = 'Lana'
last_name = 'Monteiro'
species = 'Alien'
eye_colour = 'blue'
hair_colour = 'brown'
age = 23
# Prompt user for input and Re-assign these
name = input('What new first name would you like?')
last_name = input('What new last name would you like?')
species = input('What new species would you like?')
eye_colour = input('What new eye colour would you like?')
hair_colour= input('What new hair colour would you like?')
age = int(input("what is your age? "))


## Calculate year of birth
# import time
# calculate the difference
this_year = datetime.datetime.now().year - age
# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'
print(f"Hello {name}! Welcome, your age is {age}, your eyes are {eye_colour} and your hair color is {hair_colour}. You said you we're {age} hence you were born in {this_year}!")

# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age
name = input("what is your name? ")
age = int(input("what is your age? "))

mothers_name = input("what is your mothers name? ")
mothers_age = int(input("what is your mothers age? "))
age_difference = mothers_age - age
# calculate the difference and year of birth for each
this_year = datetime.datetime.now().year - age
this_yearm = datetime.datetime.now().year - mothers_age
# print out these formated. something along the lines of:
print(f"your name is {name}, and you are {age} born on the year of {this_year}. This is {age_difference} later than {mothers_name} who was on on {this_yearm}")

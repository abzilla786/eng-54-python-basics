# practice string
# welcome to sparta - exercise

# version 1specs
# define a variable name, and assign a string with a name
from dateutil.relativedelta import relativedelta
import datetime

name1 = "Abdullah Ayyaz"

# prompt the user for input and ask the user for his/her name
# re-assign the original variable with this input

name1 = input("what is your name? ")

# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Welcome {} to our class".format(name1))
# version 2

# asl the user for a first name, save it in a variable
firstname = input("please enter your first name: ")
# ask the user for a last name, save it in a variable
lastname = input("please enter your last name: ")
# use interpolation to print the message
print(f'Welcome {firstname} {lastname}')

# calculate year of birth
# gather details on age and name

name = input("hello, whats your name? ")
age = int(input("How old are you? "))

this_year = datetime.datetime.now().year - age

# print something like
# omg <person>, you are <age> years old so you were born in <year>
print(f"OMG {name}, you are {age} years old so you were born in {this_year}!!!")

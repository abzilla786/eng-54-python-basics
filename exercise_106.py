# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

import random

guessesTaken = 0
number = random.randint(1, 20)

myName = input('Hello! What is your name?')
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    guess = int(input('Take a guess.'))
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    elif guess > number:
        print('Your guess is too high.')
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
elif guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

# We should define/assign number to a variable called magic_number
# magic_number =

# I need to ask user for input


# I need to check if this input matches a magic_number


# I need to let the user know if the response was write or not
#self five
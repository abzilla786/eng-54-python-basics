# whileloops
# syntax

# while <condition>:
    # run block of code
    # if <condition>:
    #break

counter = 0

while counter <= 10:
    print(counter)
    print('this is cool')
    counter += 1

user_input = input('you want to play? ')

while user_input == 'yes' or user_input == 'y':
    random_num = 10
    print('welcome to our random game')
    user_input = input('what is your guess')
    if user_input == random_num:
        print('WELL DONE!!!!!')
    else:
        print('sorry you were wrong')
    user_input = input('play again')


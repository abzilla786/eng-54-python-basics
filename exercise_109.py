while True:
    age = int(input('What is your age? '))
    driver_licence = input('Do you have a drivers licence? (Y/N) (Write exit to end)\n')
    if (age >= 18) and (driver_licence == 'Y'):
        print('You can vote and drive')

    elif (age >= 16) and (age < 18):
        print('you can\'t legally drink but your mates/uncles might have your back')

    elif age >= 18:
        print('You can vote')
    elif driver_licence == 'Y':
        print('You can drive')
    elif age < 18:
        print('You\'re too young, go back to school!')
    elif driver_licence == 'exit':
        break

    print('No idea mate')

# - You can vote and drive
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


#  as a user I should be able to keep being prompted for input until I say 'exit'

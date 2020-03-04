# SIMPLEST - Restaurant Waiter Helper

# User Stories
# 1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

# 2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

# 3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code


menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []
order_taken = 0
finish = 'yes'
print("Welcome to Abz Diner!")
print("Here's our menu!")

i = 0
for i in range(len(menu)):
    menu[i] = menu[i].capitalize()
    print(i +1, '-', menu[i])


while order_taken < 3 or finish == 'no':
    order = input("please write the item you would like to select: ")

    if order not in str(menu).capitalize():
        print("I'm sorry we don't serve that, what would you like? ")
        continue
    food_order.append(order)
    order_taken = order_taken + 1
    finish = input("would you like to order anything else? yes/no: ")
    if finish == "no":
        break

i = 0
print(f'perfect!, you ordered:')
for i in range(len(food_order)):
    food_order[i] = food_order[i].capitalize()
    print(food_order[i])

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything

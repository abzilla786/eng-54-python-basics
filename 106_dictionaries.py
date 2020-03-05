# Dictionaries
# work with key and value pairs
# work like a real dictionary, you just lookup the information for the specific key

# the big difference with lists is that they are organised with indexes and here we use keys

# we just make a lost of cring_landlords, but we need more information. like their phone numbers and address.

# syntax
dict_variable_name = {'key': 'value'}

boris_dict = {
    'name': 'boris',
    'l_name': 'johnson',
    'phone': '0784171157',
    'address': '10 downing street'
}
print(boris_dict)
print(type(boris_dict))

# access one key value pair
# follow the same principle of a list, but use keys not indexes
print(boris_dict['l_name'])

last_name = boris_dict['l_name']
print(last_name)

# change the value of one key value pair
boris_dict['phone'] = '+7 9374749933'
print(boris_dict['phone'])

# assign a new key value pair
boris_dict['home_phone'] = '+44 456789876545'
print(boris_dict)

boris_dict['number_budgets_passed'] = 0
print(boris_dict)
boris_dict['number_budgets_passed'] += 1
print(boris_dict)
# get all the keys
print(boris_dict.keys())


# get all the values
print(boris_dict.values())

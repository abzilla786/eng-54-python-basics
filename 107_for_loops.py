# for loops

# syntax

#for item in iteratable:
    #block of code

import time
cool_cars = ['skoda felicia fun', 'fiat abarth the old one', 'toyota corolla', 'fiat panda 4x4', 'fiat multipla']
count = 0
for car in cool_cars:
    print(count+1, '-', car)
    count += 1
    time.sleep(1)

#### for loops for dictionaries

boris_dict = {
    'name': 'boris',
    'l_name': 'johnson',
    'phone': '0784171157',
    'address': '10 downing street'
}
for key in boris_dict:
    print(key)

print(boris_dict['phone'])

for key in boris_dict:
    print(boris_dict['phone'])
    # i want each individual values
    # for this i need, dictionary + key
    print(boris_dict[key])
    print(boris_dict['phone'])

for value in boris_dict.values():
    print(value)

print('name', 'boris Johnson')

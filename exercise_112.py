# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said
# number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until
# you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu
num = ''
while num != 'penpinapplespen':
    num = input('please enter a number: ')
    if num == 'penpinapplespen':
        break
    elif int(num) % 5 is 0 and int(num) % 3 is 0:
        print("bizzuuuu")
    elif int(num) % 5 is 0:
        print("zzuuu")
    elif int(num) % 3 is 0:
        print("bizz")
    else:
        print(num)


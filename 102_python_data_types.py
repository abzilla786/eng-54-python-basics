# strings
# text and characters
# syntax
# "" and ''

# define a string
my_string = 'hey i am a cool string B)'
print(my_string)

# check its type
print(type(my_string))

# concatenation
# adding of two strings
joint_string = my_string + 'this is another string'
print(joint_string)

# example 2 of concatenation
name = 'mohammed'
welcome_text = 'welcome to spartaaaaaaa (300)'
print(welcome_text + ' ' + name)
print(welcome_text, name) #overloading the print method

# interpolation
# inserting a string inside another string
# or running python inside a string
print(f'welcome {person} to class 54, we are contested terrain')
print(f'welcome {input("whats is your name?..")} to class 54, we are contested terrain') # example of using function within a string

print('welcome {} to class 54, we are contested terrain'.format(name))


example_long_str = '   hello, this is a very baDly formated text?   '.capitalize()
print(example_long_str)
# useful methods
# are like function but belong to a specific data type
# for example, it would not make sense to try to capitalize integers


# remove trailing white spaces
example_long_str = '   hello, this is a very baDly formated text?   '.strip()
print(example_long_str)

# make it lower care
example_long_str = '   hello, this is a very baDly formated text?   '.lower()
print(example_long_str)

# make it upper case
example_long_str = '   hello, this is a very baDly formated text?   '.upper()
print(example_long_str)

# make only the first character capitalized
example_long_str = '   hello, this is a very baDly formated text?   '.capitalize()
print(example_long_str)

# make the first character of each word capitalized
example_long_str = '   hello, this is a very baDly formated text?   '.title()
print(example_long_str)

# change the ? into a !
example_long_str = '   hello, this is a very baDly formated text?   '.replace("?","!")
print(example_long_str)

#chain some methods and:
    # remove trailing white spaces
    # make it nicely formatted with only first letter capitalized
example_long_str = '   hello, this is a very baDly formated text?   '.strip().capitalize()
print(example_long_str)

# create a list with individual words
example_long_str = '   hello, this is a very baDly formated text?   '.split()
print(example_long_str)
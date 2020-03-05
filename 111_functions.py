# functions
# a function is like a machine

# it can take inputs
# and do some work (block of code)
# and it can output something different

# functions - good practices
# they do one job
# they should be testable and maintainable
#### the above avoids stringy code
# good naming convention

#### the above avoid string code - spaghetti code
# reduce technical depth

# concept of dry
# don't
# repeat
# yourself

# seperation of concern
# you seperate your code logically
# place where ou define functions
# place where you run functions
# place where you write tests
# place where you define seeds ( seeds are fake data for your app)

# syntax

# def name_of_function(arg1, arg2)
#     # block of code
#     return

# defining a simple function
# def say_hello_zeus():
#     # print('i like python')
#     return('hello zeus')
#
# # calling but not printing
# say_hello_zeus
# 'hello zeus'
#
# # calling and printing
# print(say_hello_zeus())


# defining a function with arguments
## arguments are variables that exist in the scope of a function

def full_name_formater(f_name, l_name):
    # format each name nicely
    # return a joined full name that is correctly formatted
    # i have access to the name via the arguments f_name and l_name
    # save these into variables
    formated_f_name = f_name.strip().capitalize()
    formated_l_name = l_name.strip().capitalize()

    # RETURN A JOINED FULL NAME THAT IS CORRECTLY FORMATTED
    # join the two variable into one string
    full_name = formated_f_name + ' ' + formated_l_name
    # return said string
    return full_name


# call function with names
print(full_name_formater('shannon', '    GrayHound'))


def add_funt(num1, num2):
    # i want to return the addition of two numbers
    # i have access to num 1 and num 2
    # i can save result in a variable
    result = num1 + num2
    # i can return said variable
    return result


print(add_funt(10, 300))

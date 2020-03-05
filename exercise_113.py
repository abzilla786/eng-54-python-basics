# # Python program to display the Fibonacci sequence
#
def fibornacii_sequence(n):
    if n <= 1:
        return n
    else:
        return (fibornacii_sequence(n - 1) + fibornacii_sequence(n - 2))

def fib_range_count(term):
    nterms = term

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(fibornacii_sequence(i))


print('how many fibs counts do you want')
user_term = int(input())

fib_range_count(user_term)

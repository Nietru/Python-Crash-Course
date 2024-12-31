# Numerical lists are used ALL the time in programs.
print('\n')

# Using the range() function: generates a list of numbers
for value in range(1, 5):  # generates numbers 1 - 4 because of the 'off-by-one' behavior.
    print(value)
print('\n')

for value in range(1, 6): # will give you 1 - 5
    print(value)
print('\n')

# Use the range() function to make a list of numbers:
numbers = list(range(1, 6))
print(numbers)
print('\n')

# You can also use range() to skip certain numbers in a list:
even_numbers = list(range(2, 11, 2)) # starts with 2, and then adds 2, until reaching the end number 11.
print(even_numbers)
print('\n')

# More complicated uses for example - Consider how to make a list of the first 10 square numbers (1 - 10).
# Remember that ** = exponents in python.
squares = []
for value in range(1, 11):
    square = value ** 2 # square root of each 'value': variable we gave to each of our range numbers (1-10), in the for loop.
    squares.append(square) # Each new value of 'square' is appended to the empty list 'squares'.
print(squares)
print('\n')
# To write this ^ code more precisely: omit the temporary variable 'square' and append each new value directly to the list:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print('\n')

# Python functions are helpful when working with a list of numbers. For example:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Smallest Number: ", min(digits))
print("Largest Number: ", max(digits))
print("Sum of All Numbers = ", sum(digits))
print('\n')

# List comprehensions: Like the example "squares" ^ above, list comprehensions allow you to generate those 3-4 lines of code into 1.
# List comprehensions arent generally for beginners, but you will see them alot in other people's code, so here we go (:
squares = [value**2 for value in range(1, 11)]
print(squares)
# It takes practice to write your own List Comprehensions, but they are worthwhile once you have more experience and are comfortable.
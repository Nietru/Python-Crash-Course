# The ability to change items in a list throughout the life of a program is Very useful.
# There are times when you need a list that cannot be changed. This is where Tuples are applied.
# Defining a tuple:
print('\n')
dimensions = (200, 50) # Looks like a list, but you use parenthesis instead of square brackets.
print(dimensions[0])
print(dimensions[1])
print('\n')
# Lets see what happens when we try to change something:
# dimensions[0] = 250  commented out to make following lines work.
# You cannot. Python throws an error because it is a tuple, and you cannot change a tuple.

# If you want to define a tuple with only one element, you need to include a trailing comma:
my_t = (3,) # this doesnt happen often, but just make note of it.

# Looping through all the values in a tuple is the same as a list:
for dimension in dimensions:
    print(dimension)
print('\n')

# Writing over a tuple:
# Although you cannot change a tuple, you can assign a new value to a variable that represents it:
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)  # Python doesnt throw any errors because reassigning a variable is valid.
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
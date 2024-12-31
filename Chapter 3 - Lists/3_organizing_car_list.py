# Lists will often be unpredictable in order because you cant control user input data.

# Sorting a list permanently with sort() method, is one way:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# You can sort in reverse alphabetical order with:
cars.sort(reverse=True)
print(cars,'\n')

# The sorted() function sorts a list temporarily. You can display it this way, keep the original order:
print("Here is the original list:")
print('\t',cars)
print("Here is the sorted list:")
print('\t',sorted(cars))
print("Here is the original list again:")
print('\t',cars,'\n')
# The sorted() function can also accept a reverse=True.
# Note: sorting a list in alphabetical order is more complicated when not all elements are lower-case.

# You can also print a list in reverse, without making them sorted:
print(cars)
cars.reverse()
print(cars)

# Finding the length of a list:
print(len(cars))
# When counting a list, Python starts with 1, so you shouldnt run into any "off-by-1" issues.

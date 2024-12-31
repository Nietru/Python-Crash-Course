# Most lists you create will be Dynamic: you will add and remove elements as your program runs.
# The syntax for changing a list is similar to accessing am element.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# The simplest way to add an item is to "append" it to the list with the append method:
motorcycles.append('honda')
print(motorcycles)
print('\n')


# The append method is super useful. You can start with an empty list and then add items as needed as your program runs.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print('ammended list:'.title(),motorcycles)

# Removing items from a list: 'del' statement
del motorcycles[0]
print('remove first element:'.title(),motorcycles,'\n')

# Removing items from a list: pop() method
# This is allows you to use the value after the element is removed. the del statement does not allow that value to be used later.
#   Like in a game, if you remove an enemy, you may want an explosion where the enemy used to be.
# The pop() method removes the last item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print('pop method:'.title(),motorcycles)
print('popped motorcycle:'.title(),popped_motorcycle,'\n')

# Pop() method in use: we might want to keep a list of motorcycles we bought, and say something about the last one:
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Use pop() method to remove an item from a list at any position:
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")
# Remember, once an item is popped, using pop() method, it is no longer in the list.

# You can also use the remove() method:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles,'\n')
# Remove the value 'ducati' and print a reason for removing it:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"'\nA {too_expensive.title()} is too expensive for me.")
# Note: the remove() method only removes the first 


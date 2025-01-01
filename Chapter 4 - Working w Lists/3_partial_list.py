# You can work with a specific group of items in a list. Python calls this a slice.
print('\n')

# Slicing a list, you must enter the index of the first and last items you want to include.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players,'\n')
print("Starting at beginning:")
print('\t',players[0:3])
print("Starting after first element:")
print('\t',players[1:4])
print("Omitting the first index in slice:")
print('\t',players[:4]) # If you omit the first index in a slice, python starts at the beginning of the list.
print("Omitting the last index in slice:")
print('\t',players[2:])

# Recall that -1 always accesses the last item in a list. 
# Access the last 3 players in the list:
print('\n')
print(players[-3:])
# Note: you can add a third value to a slice, like with range(), and this third value tells Python how many items to skip between items.

# Looping through a Slice:
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print('\n')
# Copying a List:
# Often you will want to use an existing list to create a new list. 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # We want to make a seperate list, of the foods our friend also likes, from our list.

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# To prove that we actually do have two seperate lists, we will add a new item to each list:
my_foods.append('canoli')
friend_foods.append('ice cream')
print('\n')
print(my_foods)
print(friend_foods)
# If we had simply set friend_foods = my_foods we would Not have two seperate lists.

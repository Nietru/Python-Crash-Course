# Start with the program you made earlier, exercise 4.1
pizzas = ['bacon-pineapple', 'mediterranean', 'chicken-alfredo']
for pizza in pizzas:
    print(pizza)
print('\n')

# Copy and paste the same list but name is friend_pizzas:
friend_pizzas = pizzas[:]     # Slice: makes new SEPERATE list, using the previous list. Not using arguments around the colon tells Python to use entire list.
# Add a new pizza to the original list:
pizzas.append('mushroom')
# Add a new pizza to the friend list:
friend_pizzas.append('sausage')
# prove that you have two seperate lists. print the message "My favorite pizzas are:" and print the list:
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for friend in friend_pizzas:
    print(friend)
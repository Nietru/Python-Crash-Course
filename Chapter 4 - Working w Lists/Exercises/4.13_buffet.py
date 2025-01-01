# A buffet restaraunt only offers five basic foods. Store these five foods in a tuple:
foods = ('spaghetti', 'chicken parm', 'salad', 'quesadilla', 'pork chop')
# use a for loop to print each food that the restaraunt serves:
print("\nFoods Served:")
for food in foods:
    print('\t',food.title())
    
# Try to modify one of the items, and be sure to make python reject the change:
# foods[0] = "tacos"  (Had to comment out to run the rest of the code)
# print(foods)  (Had to comment out to run the rest of the code)

# Now replace two items by reassigning the foods variable: Success!
foods = ('tacos', 'chicken parm', 'club sandwhich', 'quesadilla', 'pork chop')
print("\nUpdated Menu")
for food in foods:
    print('\t',food.title())

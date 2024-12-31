# Think of atleast 3 animals that have a common characteristic, and store them in a list.
print('\n')

# Use a for loop to print each animal name:
animals = ['raccoon', 'skunk', 'zebra']
for animal in animals:
    print(animal)
print('\n')
# Modify your program to print a statement about each animal.
for animal in animals:
    print(f"{animal.title()}s have a unique look!")
print('\n')
# Add a line at the end of your program stating what these animals have in common:
print(f"{animals[0].title()}s, {animals[1]}s, and {animals[2]}s all have stripes!")
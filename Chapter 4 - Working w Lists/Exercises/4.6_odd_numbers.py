# Use the third argument of the range() functions to make a list of the odd numbers from 1 to 20. Use a for loop to print each number:
print('\n')
numbers = list(range(1, 21, 2)) # starts at fist arg: 1, and adds third arg: 2, over and over until reaching the second arg: 21 (actually: 20)
for odd in numbers:
    print(odd)
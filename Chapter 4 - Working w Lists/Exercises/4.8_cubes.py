# A number raised to the third power is called a cube. In python, the cube of 2 is written: 2**3
print('\n')

# Make a list of the first ten cubes (the cubes of integers 1 through 10), and use a for loop to print the value of each cube:
cubes = []
for value in range(1, 11):
    cube = value **3
    cubes.append(cube)   
print(cubes)

print('\n')
for number in cubes:
    print(number)
# Numbers are used a bunch: to keep score in games, represent data visually, store information in web apps, etc..
# Python handles numbers differently, depending on what they're being used for.

# Integers: Add, Subract, Multiply, Divide:
print(2 + 2)
print(3-1)
print(3 * 4)
print(5/3)
print("\n")

# Python uses two multiplication symbols to represent exponents:
print(3**2)
print(3**3)
print("\n")

# Python supports the Order of Operations:
print(2 + 3 * 4)
print((2+3)*4)
print("\n")

# Floats = numbers after decimal point in Python.
# When you divide any two numbers, even if it amounts to a whole number, you will always get a float:
print(4/2)
print("\n")

# If you mix an integer and a float, in any operation, you will get a float:
print(1+2.0)
print(2*3.0)
print(3.0**2)
print("\n")

# Python ignores underscores in Numbers
universe_age = 14_000_000_00_0
print(universe_age)
print("\n")

# Multiple Assignment - You can assign more than one variable in a single line of code:
x, y, z = 0, 0, 0
print(y)
print (y+2)

# Constant: like a variable, but the value does NOT change throughout the life of the program.
# Python programmers use ALL CAPS to indicate a variable that should be treated as a Constant & never changed. DO THIS!
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
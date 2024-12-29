# In Python, [] indicate a list, and individual elements of the list are separated by commas.
print("\n")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("\n")

# List elements are numbered, and start with the number "0".
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1], bicycles[2])
print("\n")

# Use -1 to access the last item of a list. This comes in handy for longer lists.
print(bicycles[-1])
# use -2 to access the second to last item of a list:
print(bicycles[-2])
print("\n")

# Using individual items from a list:
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

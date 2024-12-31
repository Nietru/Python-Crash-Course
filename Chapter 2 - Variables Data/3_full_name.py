# Changing Case in a String

# Use the title() Method:
name = "tifannie truman"
print(name.title())

# Every Method is followed by a set of parenthesis because they often require additional info.

name = "Tifannie Truman"
print(name.upper())
print(name.lower())
# The lower() Method is useful for storing data that user's provide.

#----------------------------------------------------------------------------------------------------------------

# F-strings: The "f" stands for format because Python formats the string using your Variables. 
first_name = "genevieve"
last_name = "jeffery"
full_name = f"{first_name} {last_name}"
print(full_name)

# F-String in action:
print(f"Hello, {full_name.title()}!")

# You can also use f-strings to compose a message & then assign it to a Variable:
message = f"Hello, {full_name.title()}!"
print(message)

#----------------------------------------------------------------------------------------------------------------

# Adding Whitespace to Strings:
# \t adds a Tab space and \n adds a new Line.

print("Python")
print("\tPython\n")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Extra Whitespace can cause issues later. Python has an easy way to eliminate extra/unwanted Whitespace:

fave_language = 'python  '
print(fave_language)
fave_language.rstrip()
print(fave_language)

# lstrip() will get rid of whitespace on the left, rstrip() on the right.
# Stripping away the whitespace will be useful to do before storing user-input into a program.

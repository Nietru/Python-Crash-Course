# Looping is used CONSTANTLY in programs.

# for loop: Use when you want to do the SAME action to every element in a list.

# Using a for loop to print a list:
print('\nFor Loops:\n')
magicians = ['alice', 'david', 'maria']
for magician in magicians:  # we define the for loop here and create the variable 'magician' (this can be any name you pick).
    print(magician)  # every indented line, is inside the current for loop.
print('\n') # not indented, so is not inside the loop. This print statement is therefore not repeated more than once.
    
# You can do just about anything with each item in a list, using a for loop.
# Print a message to each magician:
for magician in magicians: # The colon tell python that the following is a for loop.
    print(f"{magician.title()}, that was a great trick!")
# Lets' add a second message, in our for loop, to each magician:
    print(f"\tI can't wait to see your next trick!")
print('\n')
print("Thankyou all for the amazing magic show!!!")

# Indentation is extremely important. Indentation errors are common so stay vigilant!
word = 'pizza'
    # print(word)  Un-comment this line and check the output.
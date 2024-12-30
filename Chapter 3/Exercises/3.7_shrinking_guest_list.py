# Your new, larger, dinner table wont arrive in time. Un-invite guests so that only two remain:
guest_list = ['genevieve', 'dahlia', 'gina', 'david']
print('original guests:'.title(),guest_list,'\n')

# Add a new message saying that you can only invite two people to dinner:
msg = "I apologize, but my new table wont arrive in time, so I can only have two people over for dinner."
print(msg,'\n')
# Use pop() to remove guests from your list one at a time, until only two names remain.
# Print a message to each removed guest letting them know you can't invite them to dinner:
uninvited_guest_1 = guest_list.pop(0)
print(f"Im sorry {uninvited_guest_1.title()}, but I cannot have you over for dinner.")
print(guest_list,'\n')
uninvited_guest_2 = guest_list.pop(1)
print(f"Im sorry {uninvited_guest_2.title()}, but I cannot have you over for dinner.")
print(guest_list,'\n')

msg = (f"Sorry for the confusion, {guest_list[0].title()} and {guest_list[1].title()}, but you are still invited to dinner!")
print(msg, '\n')

# Use del to remove the last two names from your list, so you have an empty list. Print to make sure it is empty:
del guest_list[0]
del guest_list[0]
print(guest_list)
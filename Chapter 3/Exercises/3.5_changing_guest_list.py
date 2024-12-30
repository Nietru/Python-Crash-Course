# Start with exercise 3.4:
guest_list = ['genevieve', 'dahlia', 'gina', 'david']
print(guest_list,'\n')

msg = f"Hey {guest_list[0].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[1].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[2].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[3].title()}, would you like to join me for dinner?\n"
print(msg)

# Add a print() call and state who can't make it:
unable = 'david'
guest_list.remove(unable)
print(guest_list)
print(f'\n{unable.title()} says "I cannot, I have the poops."')

# Modify your list to replace the name of the person who cannot make it, with someone else:
guest_list.append('sarah')
print(guest_list,'\n')

# Print a second set of invitations: for the new updated list:
msg = f"Hey {guest_list[0].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[1].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[2].title()}, would you like to join me for dinner?\n"
print(msg)
msg = f"Hey {guest_list[3].title()}, would you like to join me for dinner?\n"
print(msg)

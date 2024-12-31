# Think of 5 places you'd like to visit and store them in a list, make sure it is not alphabetical.
# Print the list in the original order:
locations = ['morocco', 'scottland', 'amsterdam', 'iceland', 'cuba']
print('\nOriginal List:')
print('\t',locations)
# Use sorted() to print your list in alphabetical order:
print('\nSorted List:')
print('\t',sorted(locations))
# Show the list is still in its' original order by printing it again:
print('\nOriginal List, again:')
print('\t',locations)
# Use reverse() to change the order and print:
print('\nReverse List:')
locations.reverse()
print('\t',locations)
# Use reverse() again, to show the list is back in its original order:
print('\nReverse List, again:')
locations.reverse()
print('\t',locations)
# Use sort() and print:
print('\nSort List:')
locations.sort()
print('\t',locations)
# Use sort() in reverse alphabetical order and print:
print('\nSort List, Reverse order:')
locations.sort(reverse=True)
print('\t',locations)
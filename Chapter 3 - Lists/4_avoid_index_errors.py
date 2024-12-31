motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])  *** Commented out to run rest of the code ***

# ^ This example results in an index error, because of the 'off-by-one' indexing in python(starts at 0 instead of 1).
# An index error means Python cannot find the item at the index you requested.
# You can always access the last item in a list by requesting -1, besides when a list is empty of course.
print(motorcycles[-1])

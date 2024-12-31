# Exercise 4.4 - Make a list of numbers from 1 - 1 million, and then use a for loop to print them.
# If the output is taking too long, press Ctr-C or close the output window.
million_list = range(1, 1000000001)
# for a_number in million_list:
    # print(a_number)
print('\n')
# 4.5 - Make a list of numbers from 1 - 1 million. Use min(), max(), and then the sum() function to see how quickly Python can add it:
print(min(million_list))
print(max(million_list))
print(sum(million_list))
# I timed it: 1 minute and 25 seconds on my Windows PC
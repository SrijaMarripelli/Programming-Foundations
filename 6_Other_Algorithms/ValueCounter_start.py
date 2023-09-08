# Using a hashtable to count individual items


# Define a set of items that we want to count
items = ['apple', 'pear', 'orange', 'banana', 'apple',
         'orange', 'apple', 'pear', 'banana', 'orange',
         'apple', 'kiwi', 'pear', 'apple', 'orange']

# TODO : Create a hashtable object to hold the items and counts
counter = dict()

# TODO : Iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# Print the results
print(counter)
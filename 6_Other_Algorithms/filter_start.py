# Use a hashtable to filter out duplicate items


# Define a set of items that we want to reduce duplicates
items = ['apple', 'pear', 'orange', 'banana', 'apple',
         'orange', 'apple', 'pear', 'banana', 'orange',
         'apple', 'kiwi', 'pear', 'apple', 'orange']

# TODO : Create a hashtable to perform a filter
filter = dict()

# TODO : Loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# TODO : Create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)

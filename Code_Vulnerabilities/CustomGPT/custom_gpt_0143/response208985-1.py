
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to get the counts
word_counts = Counter(flattened_list)

# Convert to a dictionary for nicer output
result = dict(word_counts)

print(result)

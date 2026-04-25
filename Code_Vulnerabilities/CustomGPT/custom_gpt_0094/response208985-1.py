
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences of each word
word_counts = Counter(flattened_list)

# Convert to a dictionary
result = dict(word_counts)

# Output the result
print(result)

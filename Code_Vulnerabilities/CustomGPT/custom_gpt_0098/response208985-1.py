
from collections import Counter

# Sample input
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences
word_counts = Counter(flattened_list)

# Convert Counter to a dictionary (optional)
word_counts_dict = dict(word_counts)

print(word_counts_dict)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

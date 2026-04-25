
from collections import Counter

# Given list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [item for sublist in list_of_lists for item in sublist]

# Use Counter to count occurrences
word_counts = Counter(flattened_list)

# Convert Counter to a dictionary
word_counts_dict = dict(word_counts)

print(word_counts_dict)

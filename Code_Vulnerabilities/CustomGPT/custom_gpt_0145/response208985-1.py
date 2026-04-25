
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [item for sublist in list_of_lists for item in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened_list)

# Convert to a dictionary
word_count_dict = dict(word_count)

print(word_count_dict)


from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened_list)

# Convert to dictionary (optional)
word_count_dict = dict(word_count)

print(word_count_dict)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

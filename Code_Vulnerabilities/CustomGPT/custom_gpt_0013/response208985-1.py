
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences
word_count = Counter(flattened_list)

# Convert to dictionary for display
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

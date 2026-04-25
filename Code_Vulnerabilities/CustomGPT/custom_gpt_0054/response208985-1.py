
from collections import Counter

# Given list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences of each word
word_count = Counter(flattened_list)

# Convert to a dictionary if needed
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

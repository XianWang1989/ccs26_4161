
from collections import Counter

# List of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Using Counter to count occurrences
word_count = Counter(flattened_list)

# Converting to a dictionary if needed
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

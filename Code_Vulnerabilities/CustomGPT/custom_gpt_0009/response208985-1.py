
from collections import Counter

# Your list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flat_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flat_list)

# Convert to a dictionary for a more readable output
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

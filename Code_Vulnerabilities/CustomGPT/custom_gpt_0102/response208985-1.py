
from collections import Counter

# Input: list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in lists for word in sublist]

# Count occurrences
word_count = Counter(flattened)

# Convert to dictionary
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

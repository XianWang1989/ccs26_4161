
from collections import Counter

# Sample list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists using a list comprehension
flattened = [word for sublist in lists for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened)

# Convert to a regular dictionary if desired
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Sample input
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in lists for word in sublist)

# Convert to dictionary format
result = dict(word_counts)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

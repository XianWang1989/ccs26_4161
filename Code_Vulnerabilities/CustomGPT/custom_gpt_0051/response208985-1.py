
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in list_of_lists for word in sublist)

# Convert to a dictionary (optional, as Counter is already a dict subclass)
result = dict(word_counts)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Your list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list and count occurrences
word_count = Counter(word for sublist in data for word in sublist)

# Convert counter to a dictionary
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

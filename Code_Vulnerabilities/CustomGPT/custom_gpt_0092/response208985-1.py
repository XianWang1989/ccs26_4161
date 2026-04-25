
from collections import Counter

# Sample list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in data for word in sublist]

# Use Counter to count the occurrences
word_count = Counter(flattened_list)

# Convert to dictionary (optional, as Counter is a subclass of dict)
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Example list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in data for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened)

# Convert to a dictionary to get the desired output format
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

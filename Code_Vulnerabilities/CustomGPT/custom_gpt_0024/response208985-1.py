
from collections import Counter

# Example list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in lists for word in sublist]

# Count the occurrences of each word
word_count = Counter(flattened)

# Convert Counter to a regular dictionary if needed
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

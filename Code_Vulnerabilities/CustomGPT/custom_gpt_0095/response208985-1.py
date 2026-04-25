
from collections import Counter

# List of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flat_list = [word for sublist in data for word in sublist]

# Count occurrences using Counter
word_count = Counter(flat_list)

# Convert to dictionary
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

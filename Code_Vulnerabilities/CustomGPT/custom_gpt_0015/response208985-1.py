
from collections import Counter

# Sample list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list
flat_list = [word for sublist in data for word in sublist]

# Count occurrences using Counter
word_count = Counter(flat_list)

# Convert to dictionary for a nicer output
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

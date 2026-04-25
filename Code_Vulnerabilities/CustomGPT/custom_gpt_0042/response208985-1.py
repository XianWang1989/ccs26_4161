
from collections import Counter

# Example input: a list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in data for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened)

# Convert Counter to a dictionary (optional)
word_count_dict = dict(word_count)

print(word_count_dict)

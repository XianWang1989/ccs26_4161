
from collections import Counter

# Given list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in lists for word in sublist)

# Convert to dictionary for better readability
result = dict(word_counts)

print(result)

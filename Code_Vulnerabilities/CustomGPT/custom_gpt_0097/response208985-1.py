
from collections import Counter

# Example list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in lists for word in sublist)

# Convert to a dictionary for the desired format
result = dict(word_count)

print(result)

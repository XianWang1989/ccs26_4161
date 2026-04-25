
from collections import Counter

# List of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in lists for word in sublist)

# Print the result
print(dict(word_count))

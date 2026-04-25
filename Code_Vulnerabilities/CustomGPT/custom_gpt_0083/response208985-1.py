
from collections import Counter

# Sample input
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to a dictionary
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
flat_list = [word for sublist in list_of_lists for word in sublist]
word_count = Counter(flat_list)

# Convert to dictionary (optional, as Counter is already a dict subclass)
result = dict(word_count)

print(result)

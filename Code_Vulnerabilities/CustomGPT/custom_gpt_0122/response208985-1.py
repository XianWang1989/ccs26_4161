
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists and counting words
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Converting to a dictionary
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

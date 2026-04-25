
from collections import Counter

# Sample input
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Counting occurrences
word_count = Counter(flattened_list)

# Converting to a dictionary
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

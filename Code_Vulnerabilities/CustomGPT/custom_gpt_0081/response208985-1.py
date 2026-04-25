
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences with Counter
word_count = Counter(flattened_list)

# Convert Counter object to a dictionary
word_count_dict = dict(word_count)

print(word_count_dict)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

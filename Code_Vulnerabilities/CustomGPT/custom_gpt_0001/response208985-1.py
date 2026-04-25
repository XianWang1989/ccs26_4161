
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences of each word
word_counts = Counter(flattened_list)

# Convert to dictionary
result = dict(word_counts)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Given list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences using Counter
word_counts = Counter(flattened_list)

# Convert to a dictionary for a cleaner output
result = dict(word_counts)

# Print the result
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Example list of lists
lists_of_words = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in lists_of_words for word in sublist]

# Count occurrences
word_count = Counter(flattened_list)

# Convert to dictionary
result = dict(word_count)

print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

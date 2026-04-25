
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened)

# Convert the Counter to a dictionary
word_count_dict = dict(word_count)

# Output the result
print(word_count_dict)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

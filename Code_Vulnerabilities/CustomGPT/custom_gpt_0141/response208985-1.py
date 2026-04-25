
from collections import Counter

# Sample input: a list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists into a single list
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences of each word
word_count = Counter(flattened_list)

# Convert Counter object to a regular dict for better readability
word_count_dict = dict(word_count)

# Print the result
print(word_count_dict)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

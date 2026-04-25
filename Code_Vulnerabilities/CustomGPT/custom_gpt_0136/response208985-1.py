
from collections import Counter

# Sample input: list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences
word_counts = Counter(flattened_list)

# Convert to dict for the desired output format
result = dict(word_counts)

print(result)


from collections import Counter

# Sample input: a list of lists
lists_of_words = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in lists_of_words for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flattened_list)

# Convert Counter to a regular dictionary
count_dict = dict(word_count)

print(count_dict)

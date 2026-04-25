
from collections import Counter

# Given list of lists
lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flat_list = [word for sublist in lists for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flat_list)

# Convert to dictionary if needed
word_count_dict = dict(word_count)

print(word_count_dict)

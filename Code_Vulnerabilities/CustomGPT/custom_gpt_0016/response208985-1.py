
from collections import Counter

# Sample input
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences using Counter
word_counts = Counter(flattened_list)

# Convert Counter to a dictionary (optional)
word_count_dict = dict(word_counts)

print(word_count_dict)

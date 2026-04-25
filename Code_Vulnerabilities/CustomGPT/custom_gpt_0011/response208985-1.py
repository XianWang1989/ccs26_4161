
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences of each word
word_counts = Counter(flattened_list)

# Convert to a dictionary (optional, as Counter itself is a subclass of dict)
word_count_dict = dict(word_counts)

print(word_count_dict)

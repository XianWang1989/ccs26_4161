
from collections import Counter

# Define your list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences of each word
word_counts = Counter(flattened_list)

# Convert to a dictionary (optional, as Counter is a subclass of dict)
word_counts_dict = dict(word_counts)

# Output the result
print(word_counts_dict)

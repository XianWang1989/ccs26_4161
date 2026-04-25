
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences of each word
word_count = Counter(flattened_list)

# Convert to a dictionary for display
word_count_dict = dict(word_count)

print(word_count_dict)

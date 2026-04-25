
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Counting the occurrences of each word
word_counts = Counter(flattened_list)

# Convert to dictionary if needed
word_counts_dict = dict(word_counts)

print(word_counts_dict)

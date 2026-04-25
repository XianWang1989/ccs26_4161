
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in list_of_lists for word in sublist)

# Convert the Counter to a dictionary for easier reading (optional)
word_counts_dict = dict(word_counts)

print(word_counts_dict)

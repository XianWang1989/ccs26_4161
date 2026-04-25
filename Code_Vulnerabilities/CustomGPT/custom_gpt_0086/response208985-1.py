
from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count the occurrences
word_counts = Counter(word for sublist in list_of_lists for word in sublist)

# Convert to a dictionary for a cleaner output
result = dict(word_counts)

print(result)

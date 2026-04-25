
from collections import Counter

# Sample input: list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to a dictionary
result = dict(word_counts)

print(result)


from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list and count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to a dictionary
result = dict(word_count)

print(result)

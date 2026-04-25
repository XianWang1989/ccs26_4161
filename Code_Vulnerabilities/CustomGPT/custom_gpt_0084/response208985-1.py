
from collections import Counter

# Given list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert to dictionary if needed
result = dict(word_count)

print(result)


from collections import Counter

# Given list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in data for word in sublist)

# Converting Counter to a dictionary
result = dict(word_count)

print(result)

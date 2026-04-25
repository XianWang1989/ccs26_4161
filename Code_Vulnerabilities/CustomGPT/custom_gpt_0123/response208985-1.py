
from collections import Counter

# Example list of lists
lists_of_words = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_counts = Counter(word for sublist in lists_of_words for word in sublist)

# Convert Counter to a dictionary
result = dict(word_counts)

print(result)

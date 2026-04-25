
from collections import Counter

# Example list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened = [word for sublist in data for word in sublist]

# Use Counter to count occurrences of each word
word_counts = Counter(flattened)

# Convert to a dictionary (if needed) and print the result
result = dict(word_counts)
print(result)

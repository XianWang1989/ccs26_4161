
from collections import Counter

# Example list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in data for word in sublist]

# Using Counter to count occurrences
word_count = Counter(flattened_list)

# Displaying the result
print(dict(word_count))

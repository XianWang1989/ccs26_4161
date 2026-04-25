
from collections import Counter

# Input: list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in data for word in sublist]

# Counting occurrences
word_count = Counter(flattened_list)

# Converting to dictionary
result = dict(word_count)

print(result)

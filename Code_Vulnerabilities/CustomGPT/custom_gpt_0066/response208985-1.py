
from collections import Counter

# Sample list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flat_list = [word for sublist in data for word in sublist]

# Use Counter to count occurrences
word_count = Counter(flat_list)

# Convert to dictionary format for better readability
result = dict(word_count)

print(result)

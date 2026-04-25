
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list and create a Counter
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to a regular dictionary (optional)
result = dict(word_count)

# Print the result
print(result)

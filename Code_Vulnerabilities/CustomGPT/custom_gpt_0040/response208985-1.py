
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flat_list = [word for sublist in list_of_lists for word in sublist]

# Count occurrences
word_count = Counter(flat_list)

# Convert to dictionary to display the counts
result = dict(word_count)

print(result)

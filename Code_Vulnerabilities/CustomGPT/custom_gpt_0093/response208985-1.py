
from collections import Counter

# Sample list of lists
data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in data for word in sublist]

# Count occurrences using Counter
word_count = Counter(flattened_list)

# Convert to a dictionary if needed
word_count_dict = dict(word_count)

print(word_count_dict)

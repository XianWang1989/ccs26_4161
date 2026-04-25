
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert to a dictionary for easier readability
word_count_dict = dict(word_count)

# Output the result
print(word_count_dict)

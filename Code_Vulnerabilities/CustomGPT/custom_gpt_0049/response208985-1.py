
from collections import Counter

# Sample input: list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists using a list comprehension
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count occurrences of each word
word_count = Counter(flattened_list)

# Convert to a dictionary (optional, since Counter is a subclass of dict)
word_count_dict = dict(word_count)

print(word_count_dict)

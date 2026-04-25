
from collections import Counter

# Sample input: list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists using a list comprehension
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Using Counter to count occurrences
word_count = Counter(flattened_list)

# Converting the result to a dictionary
result = dict(word_count)

print(result)


from collections import Counter

# Example list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and use Counter to count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter object to a dictionary
result = dict(word_count)

print(result)  # Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and count occurrences
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to dictionary for a cleaner output
count_dict = dict(word_count)

print(count_dict)

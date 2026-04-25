
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and create a Counter
word_count = Counter(word for sublist in list_of_lists for word in sublist)

# Convert Counter to a dictionary and print it
word_count_dict = dict(word_count)
print(word_count_dict)

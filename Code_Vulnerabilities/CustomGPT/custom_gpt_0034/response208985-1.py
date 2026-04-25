
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flattening the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Counting occurrences
word_count = Counter(flattened_list)

# Converting to a dictionary for better readability
word_count_dict = dict(word_count)

print(word_count_dict)

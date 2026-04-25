
from collections import Counter

# Sample list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Use Counter to count the occurrences of each word
word_count = Counter(flattened_list)

# Convert the Counter object to a dictionary
result = dict(word_count)

print(result)

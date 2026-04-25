
from collections import Counter

# Example list of lists
lists_of_words = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Flatten the list of lists and create a Counter
word_count = Counter(word for sublist in lists_of_words for word in sublist)

# Convert to a dictionary for better readability
word_count_dict = dict(word_count)

print(word_count_dict)

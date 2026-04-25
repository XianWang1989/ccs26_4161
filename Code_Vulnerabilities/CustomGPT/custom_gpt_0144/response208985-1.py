from collections import Counter

list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
# Flatten the list of lists
flattened = [item for sublist in list_of_lists for item in sublist]
# Use Counter to count occurrences
word_counts = Counter(flattened)

print(word_counts)

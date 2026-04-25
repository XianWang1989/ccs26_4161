
from collections import Counter

# Input: a list of lists
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]

# Step 1: Flatten the list of lists
flattened_list = [word for sublist in list_of_lists for word in sublist]

# Step 2: Use Counter to count occurrences of each word
word_count = Counter(flattened_list)

# Convert the Counter to a dictionary for better readability
word_count_dict = dict(word_count)

# Output the result
print(word_count_dict)

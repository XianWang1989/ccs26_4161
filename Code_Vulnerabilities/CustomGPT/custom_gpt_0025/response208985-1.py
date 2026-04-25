
from collections import Counter

def count_words(list_of_lists):
    # Flatten the list of lists
    flattened_list = [word for sublist in list_of_lists for word in sublist]
    # Use Counter to count occurrences
    return dict(Counter(flattened_list))

# Example usage
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
word_count = count_words(list_of_lists)
print(word_count)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

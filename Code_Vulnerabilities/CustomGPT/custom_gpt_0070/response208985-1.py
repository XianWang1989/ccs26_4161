
from collections import Counter

def count_words(lists):
    # Flatten the list of lists
    flat_list = [word for sublist in lists for word in sublist]
    # Use Counter to count occurrences
    return dict(Counter(flat_list))

# Example usage
example_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
word_counts = count_words(example_lists)
print(word_counts)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

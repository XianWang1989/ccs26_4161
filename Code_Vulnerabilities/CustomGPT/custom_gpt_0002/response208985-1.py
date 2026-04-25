
from collections import Counter

def count_words(list_of_lists):
    # Flatten the list of lists
    flattened = [word for sublist in list_of_lists for word in sublist]
    # Use Counter to count occurrences
    return dict(Counter(flattened))

# Example usage
input_data = [['a','b','a','c'], ['a','b','c','d']]
result = count_words(input_data)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

def count_words(list_of_lists):
    # Flatten the list of lists
    flattened_list = [word for sublist in list_of_lists for word in sublist]
    # Use Counter to count occurrences
    count_dict = Counter(flattened_list)
    return dict(count_dict)

# Example usage
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(list_of_lists)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

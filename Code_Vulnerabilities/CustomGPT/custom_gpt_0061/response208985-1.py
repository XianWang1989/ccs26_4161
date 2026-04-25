
from collections import Counter

def count_words(list_of_lists):
    # Flatten the list of lists into a single list
    flat_list = [word for sublist in list_of_lists for word in sublist]
    # Use Counter to count occurrences of each word
    word_count = Counter(flat_list)
    return dict(word_count)

# Example usage
input_data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(input_data)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

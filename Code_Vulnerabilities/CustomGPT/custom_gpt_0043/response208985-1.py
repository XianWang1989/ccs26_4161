
from collections import Counter

def count_words(lists):
    # Flatten the list of lists using a list comprehension
    flattened_list = [word for sublist in lists for word in sublist]

    # Use Counter to count occurrences of each word
    word_count = Counter(flattened_list)

    return dict(word_count)  # Convert to a dictionary for easier display

# Example usage
lists_of_words = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(lists_of_words)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}


from collections import Counter

# Function to count occurrences of each word in a list of lists
def count_words(list_of_lists):
    # Flatten the list of lists
    words_flat = [word for sublist in list_of_lists for word in sublist]
    # Use Counter to count occurrences
    word_count = Counter(words_flat)
    return dict(word_count)

# Example usage
list_of_lists = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(list_of_lists)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

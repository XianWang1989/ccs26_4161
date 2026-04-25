
from collections import Counter

def count_words(list_of_lists):
    # Initialize a Counter object to keep track of counts
    word_count = Counter()

    # Iterate through each sublist
    for sublist in list_of_lists:
        # Update the Counter with the words in the current sublist
        word_count.update(sublist)

    # Convert the Counter to a regular dictionary for easier readability
    return dict(word_count)

# Example usage
input_data = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(input_data)
print(result)  # Output: {'a': 2, 'b': 2, 'c': 2, 'd': 1}

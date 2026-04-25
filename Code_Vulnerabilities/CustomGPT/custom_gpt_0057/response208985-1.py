
from collections import Counter

def count_words(lists):
    word_counter = Counter()
    for sublist in lists:
        word_counter.update(sublist)
    return dict(word_counter)

example_input = [['a', 'b', 'a', 'c'], ['a', 'b', 'c', 'd']]
result = count_words(example_input)
print(result)

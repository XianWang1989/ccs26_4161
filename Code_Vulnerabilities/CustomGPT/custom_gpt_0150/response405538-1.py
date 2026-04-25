
import ahocorasick

# Build the Aho-Corasick trie
A = ahocorasick.Automaton()
sub_strings = ["some", "text", "large", "here"]

for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

A.make_automaton()

# The large string
string = "some large text here"

# Search for substrings in the large string
for end_index, (index, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1  # Calculate start index
    print(f"'{substring}' found at position {start_index}")

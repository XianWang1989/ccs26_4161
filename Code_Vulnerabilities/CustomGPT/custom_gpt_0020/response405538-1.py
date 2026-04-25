
import ahocorasick

# Sample larger string
string = "some large text here and some more text here"
# List of smaller substrings
sub_strings = ["some", "text", "large", "not_in_string"]

# Create an Aho-Corasick trie
A = ahocorasick.Automaton()

# Add substrings to the trie
for idx, sub_str in enumerate(sub_strings):
    A.add_word(sub_str, (idx, sub_str))

# Finalize the trie
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, sub_str) in A.iter(string):
    start_index = end_index - len(sub_str) + 1
    print(f"Substring '{sub_str}' found at position {start_index}")

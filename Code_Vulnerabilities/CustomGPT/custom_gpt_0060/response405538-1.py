
import ahocorasick

# Sample string and substrings
string = "some large text here"
sub_strings = ["some", "text", "large", "notfound"]

# Create an Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the Aho-Corasick automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1  # Calculate the start index
    print(f"Substring '{substring}' found at position {start_index}")

# This will print the starting index of each substring found in the string

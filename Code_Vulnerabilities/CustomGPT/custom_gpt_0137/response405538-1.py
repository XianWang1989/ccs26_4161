
from ahocorasick import Automaton

# Create an instance of the Aho-Corasick automaton
A = Automaton()

# Your large string
large_string = "some large text here"
# List of substrings to find
sub_strings = ["some", "text"]

# Add each substring to the automaton
for substring in sub_strings:
    A.add_word(substring, substring)

# Finalize the automaton (construct the Aho-Corasick structure)
A.make_automaton()

# Search for all substrings in the large string
for end_index, original_value in A.iter(large_string):
    start_index = end_index - len(original_value) + 1  # calculate the start index
    print(f"'{original_value}' found at position {start_index}")


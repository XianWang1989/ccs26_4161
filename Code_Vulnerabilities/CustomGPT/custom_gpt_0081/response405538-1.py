
import ahocorasick

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Your large string
large_string = "some large text here"
# List of substrings to search for
sub_strings = ["some", "text"]

# Add substrings to the automaton
for substring in sub_strings:
    A.add_word(substring, substring)

# Finalize the automaton
A.make_automaton()

# Find and print the positions of the substrings
for end_index, original_value in A.iter(large_string):
    start_index = end_index - len(original_value) + 1
    print(f"{original_value} found at position {start_index}")

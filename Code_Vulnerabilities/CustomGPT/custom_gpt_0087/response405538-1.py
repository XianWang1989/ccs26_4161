
import ahocorasick

# Create a large string
large_string = "some large text here"

# List of substrings to search
sub_strings = ["some", "text", "large"]

# Initialize Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton to prepare for searching
A.make_automaton()

# Search for substrings in the large string
for end_index, (idx, substring) in A.iter(large_string):
    start_index = end_index - len(substring) + 1
    print(f"Found '{substring}' at position {start_index}")

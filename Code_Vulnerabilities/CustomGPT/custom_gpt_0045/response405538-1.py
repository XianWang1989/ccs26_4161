
import ahocorasick

# Define the large string and list of substrings.
string = "some large text here"
sub_strings = ["some", "text", "large"]

# Create an Aho-Corasick Automaton.
A = ahocorasick.Automaton()

# Add all substrings to the Automaton.
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the Automaton.
A.make_automaton()

# Search for substrings in the larger string and print their positions.
for end_index, (index, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"Substring: '{original_value}' found at position: {start_index}")

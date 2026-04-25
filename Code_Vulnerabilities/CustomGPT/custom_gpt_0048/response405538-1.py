
import ahocorasick

# Define the large string and the list of substrings
large_string = "some large text here"
sub_strings = ["some", "text", "large", "missing"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for i, substring in enumerate(sub_strings):
    A.add_word(substring, (i, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, (index, original_value) in A.iter(large_string):
    start_index = end_index - len(original_value) + 1
    print(f"Substring '{original_value}' found at position {start_index}")

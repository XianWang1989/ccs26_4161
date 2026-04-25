
import ahocorasick

# Your large string
string = "some large text here with some extra words and text to find"

# List of substrings to search
sub_strings = ["some", "text", "extra", "find"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search in the large string
for end_index, (idx, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"Substring '{original_value}' found at positions {start_index}-{end_index}")


import ahocorasick

# Create the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Add substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, (idx, found_substring) in A.iter(string):
    start_index = end_index - len(found_substring) + 1
    print(f"{found_substring} found at position {start_index}")

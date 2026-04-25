
import ahocorasick

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Your large string
string = "some large text here"

# List of substrings to search for
sub_strings = ["some", "text"]

# Add each substring to the automaton
for sub in sub_strings:
    A.add_word(sub, sub)

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, original_value in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(original_value, start_index)

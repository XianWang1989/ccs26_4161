
import ahocorasick

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Define the large string and the list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Add each substring to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))  # (index, substring)

# Finalize the Aho-Corasick automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"{original_value} found at position {start_index}")

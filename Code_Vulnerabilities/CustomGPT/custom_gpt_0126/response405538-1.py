
import ahocorasick

# Define the large string and list of substrings
string = "some large text here"
sub_strings = ["some", "text", "large", "missing"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1
    print(f"{substring}: starts at {start_index}, ends at {end_index}")

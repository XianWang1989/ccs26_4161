
import ahocorasick

# Initialize the large string and substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, sub) in A.iter(string):
    print(f"{sub} found at position {end_index - len(sub) + 1}")

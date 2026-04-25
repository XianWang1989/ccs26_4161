
import ahocorasick

# Create a large string and a list of substrings
string = "some large text here, some more text, and some extra text"
sub_strings = ["some", "text", "large", "extra"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the main string
for end_index, (idx, sub) in A.iter(string):
    start_index = end_index - len(sub) + 1
    print(f"'{sub}' found at position: {start_index}")

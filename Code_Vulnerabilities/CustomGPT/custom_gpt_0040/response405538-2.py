
from ahocorasick import Automaton

string = "some large text here"
sub_strings = ["some", "text"]

# Create an Aho-Corasick automaton
A = Automaton()

# Add all substrings to the automaton
for sub in sub_strings:
    A.add_word(sub, (sub, -1))  # Store the word and a placeholder for position

A.make_automaton()

# Search for substrings in the main string
for end_index, (sub_string, _) in A.iter(string):
    start_index = end_index - len(sub_string) + 1
    print(f"'{sub_string}' found at position {start_index}")

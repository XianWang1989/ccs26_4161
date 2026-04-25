
import ahocorasick

# Your large string
string = "some large text here, including some more text to analyze"

# List of substrings
sub_strings = ["some", "text", "analyze", "large", "notfound"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton
A.make_automaton()

# Search for the substrings and get their positions
for end_index, (idx, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1
    print(f"Substring '{substring}' found at position {start_index}")

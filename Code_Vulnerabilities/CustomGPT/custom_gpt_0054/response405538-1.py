
import ahocorasick

# Initialize the Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Define your large string and substrings
string = "some large text here with some other text and some more text"
sub_strings = ["some", "text"]

# Add substrings to the automaton
for substring in sub_strings:
    A.add_word(substring, substring)

# Finalize the automaton to prepare it for searching
A.make_automaton()

# Search for substrings in the string
for end_index, original_value in A.iter(string):
    print(f"{original_value} found at position {end_index - len(original_value) + 1}")

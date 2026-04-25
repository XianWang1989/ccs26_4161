
import ahocorasick

# Create an instance of the Aho-Corasick automaton
A = ahocorasick.Automaton()

# The large string we want to search in
string = "some large text here"

# List of substrings to search for
sub_strings = ["some", "text"]

# Add each substring to the automaton
for substring in sub_strings:
    A.add_word(substring, substring)

# Finalize the automaton to prepare it for search
A.make_automaton()

# Search the large string with the automaton
for end_index, original_value in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"{original_value}: Position {start_index}")


import ahocorasick

# Create a large string
string = "some large text here. some more text is here."

# Create a list of substrings to find
sub_strings = ["some", "text", "here", "more", "notfound"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for index, sub_string in enumerate(sub_strings):
    A.add_word(sub_string, (index, sub_string))

# Finalize the automaton
A.make_automaton()

# Search for the substrings in the main string
for end_index, (index, sub_string) in A.iter(string):
    start_index = end_index - len(sub_string) + 1
    print(f"'{sub_string}' found at position: {start_index}")

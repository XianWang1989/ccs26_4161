
import ahocorasick

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Your large string
string = "some large text here with some more text and even more examples of text here"
# List of substrings to search
sub_strings = ["some", "text", "large", "examples", "notfound"]

# Add all substrings to the automaton
for idx, substr in enumerate(sub_strings):
    A.add_word(substr, (idx, substr))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, substr) in A.iter(string):
    start_index = end_index - len(substr) + 1
    print(f"Substring '{substr}' found at position {start_index}")


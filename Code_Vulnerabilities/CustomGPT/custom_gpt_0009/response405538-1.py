
import ahocorasick

# Create the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Your large string
string = "some large text here with some more text"

# Add your substrings to the automaton
sub_strings = ["some", "text", "more"]
for idx, substr in enumerate(sub_strings):
    A.add_word(substr, (idx, substr))

# Finalize the automaton
A.make_automaton()

# Search the text
for end_index, (idx, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"'{original_value}' found at {start_index}")

# Note: You may want to handle the output formatting to suit your needs.

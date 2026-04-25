
import ahocorasick

# Initialize the Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Large string to search in
string = "some large text here"

# List of substrings to search for
sub_strings = ["some", "text"]

# Add substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search through the main string
for end_index, (idx, original_value) in A.iter(string):
    print(f"Found '{original_value}' at position {end_index - len(original_value) + 1}")

# Output:
# Found 'some' at position 0
# Found 'text' at position 10

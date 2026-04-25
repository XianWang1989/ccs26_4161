
import ahocorasick

# Create a large string
string = "some large text here, some additional text for testing purposes."

# List of substrings
sub_strings = ["some", "text", "additional", "testing", "purposes"]

# Initialize Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (idx, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"Substring '{original_value}' found at position {start_index}")

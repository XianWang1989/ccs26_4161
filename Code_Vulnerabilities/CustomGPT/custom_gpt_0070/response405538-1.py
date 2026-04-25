
import ahocorasick

# Create a large string
string = "some large text here and some other text for searching"
# A large number of substrings
sub_strings = ["some", "text", "large", "other", "missing"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add each substring to the automaton
for i, sub_string in enumerate(sub_strings):
    A.add_word(sub_string, (i, sub_string))

# Finalize the automaton
A.make_automaton()

# Search in the main string
for end_index, (i, original_value) in A.iter(string):
    start_index = end_index - len(original_value) + 1
    print(f"'{original_value}' found at positions {start_index} to {end_index}")

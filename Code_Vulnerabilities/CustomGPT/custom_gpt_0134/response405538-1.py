
import ahocorasick

# Initialize the large string and the list of substrings
string = "some large text here"
sub_strings = ["some", "text", "large", "not_found"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add each substring to the automaton
for idx, substr in enumerate(sub_strings):
    A.add_word(substr, (idx, substr))

# Finalize the automaton
A.make_automaton()

# Search for patterns in the large string
for end_index, (idx, found_substring) in A.iter(string):
    start_index = end_index - len(found_substring) + 1
    print(f"Found '{found_substring}' at position {start_index}")

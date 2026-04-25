
import ahocorasick

# Large string
large_string = "some large text here with some other content"
sub_strings = ["some", "text", "other"]

# Create an Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, (idx, original_value) in A.iter(large_string):
    start_index = end_index - len(original_value) + 1
    print(f"Substring '{original_value}' found at position {start_index}")

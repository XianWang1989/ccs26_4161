
import ahocorasick

# Create a large string and a list of substrings
large_string = "some large text here with some other text"
sub_strings = ["some", "text", "large", "other"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add substrings to the automaton
for i, substring in enumerate(sub_strings):
    A.add_word(substring, (i, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the larger string
for end_index, (insert_order, original_value) in A.iter(large_string):
    start_index = end_index - len(original_value) + 1
    print(f"{original_value}: {start_index}")


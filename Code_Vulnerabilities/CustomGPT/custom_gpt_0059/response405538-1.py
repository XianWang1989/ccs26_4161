
import ahocorasick

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Large string to search in
large_string = "some large text here with some random text for testing purposes."

# List of substrings
sub_strings = ["some", "text"]

# Adding substrings to the automaton
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the automaton
A.make_automaton()

# Search the large string
for end_index, (index, substring) in A.iter(large_string):
    start_index = end_index - len(substring) + 1
    print(f"'{substring}' found at position {start_index}")

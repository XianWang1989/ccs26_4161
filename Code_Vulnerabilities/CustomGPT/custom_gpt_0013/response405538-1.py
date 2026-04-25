
import ahocorasick

# Your large string
large_string = "some large text here with some more text and other content"

# List of substrings to search for
sub_strings = ["some", "text", "large", "other"]

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, (index, substring) in A.iter(large_string):
    start_index = end_index - len(substring) + 1  # Calculate the start index
    print(f"Found '{substring}' at position {start_index}")


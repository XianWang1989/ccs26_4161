
import ahocorasick

# Initialize the large string and the list of substrings
large_string = "some large text here that includes some other text"
sub_strings = ["some", "text", "large", "doesnotexist"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, (index, substring) in A.iter(large_string):
    start_index = end_index - len(substring) + 1
    print(f"'{substring}' found at position {start_index}")


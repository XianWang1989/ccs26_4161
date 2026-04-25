
import ahocorasick

# Define the large string
string = "some large text here"

# List of substrings to search
sub_strings = ["some", "text", "large"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add each substring to the automaton with its index
for index, substring in enumerate(sub_strings):
    A.add_word(substring, index)

# Finalize the automaton
A.make_automaton()

# Search for substrings in the large string
for end_index, original_index in A.iter(string):
    start_index = end_index - len(sub_strings[original_index]) + 1
    print(f"{sub_strings[original_index]} found at position {start_index}")

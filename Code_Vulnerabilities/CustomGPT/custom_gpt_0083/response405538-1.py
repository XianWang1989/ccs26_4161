
import ahocorasick

# Initialize the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
sub_strings = ["some", "text"]
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton
A.make_automaton()

# The large string to search
string = "some large text here"

# Search for each substring and print their positions
for end_index, (idx, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1
    print(f"{substring}: {start_index}")

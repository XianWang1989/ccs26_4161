
import ahocorasick

# Create the Aho-Corasick automaton
A = ahocorasick.Automaton()

# Insert substrings into the automaton
sub_strings = ["some", "text", "large", "here"]  # Add more substrings as needed
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the automaton
A.make_automaton()

# Large string to be searched
string = "some large text here"

# Searching for substrings
for end_index, (index, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1
    print(f"'{substring}' found at position: {start_index}")

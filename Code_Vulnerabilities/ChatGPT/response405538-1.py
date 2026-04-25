
import ahocorasick

# Create the Aho-Corasick automaton
A = ahocorasick.Automaton()

# The larger string to search in
string = "some large text here"

# List of substrings to search for
sub_strings = ["some", "text"]

# Add all substrings to the automaton
for idx, substring in enumerate(sub_strings):
    A.add_word(substring, (idx, substring))

# Finalize the automaton
A.make_automaton()

# Searching for substrings in the large string
found_positions = []
for end_index, (idx, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1  # Calculate the start index
    found_positions.append((substring, start_index))

# Print the results
for substring, position in found_positions:
    print(substring, position)

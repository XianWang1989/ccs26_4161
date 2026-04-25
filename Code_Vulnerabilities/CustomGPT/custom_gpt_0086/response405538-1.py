
import ahocorasick

# Create a large string and list of substrings
string = "some large text here" * 1000  # Example large string
sub_strings = ["some", "text", "large", "here"]

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for idx, sub in enumerate(sub_strings):
    A.add_word(sub, (idx, sub))

# Finalize the automaton
A.make_automaton()

# Search for the substrings in the large string
results = {}
for end_index, (idx, sub) in A.iter(string):
    start_index = end_index - len(sub) + 1
    results[sub] = start_index

# Print the results
for sub, pos in results.items():
    print(f"{sub} found at position {pos}")

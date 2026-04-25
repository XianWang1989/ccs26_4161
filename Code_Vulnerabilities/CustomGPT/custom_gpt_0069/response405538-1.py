
import ahocorasick

# Your large string
string = "some large text here with more text and some other text"
# List of substrings to search
sub_strings = ["some", "text", "large", "other"]

# Initialize the Aho-Corasick Automaton
A = ahocorasick.Automaton()

# Add your substrings to the automaton
for i, substr in enumerate(sub_strings):
    A.add_word(substr, (i, substr))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the main string
for end_index, (i, substr) in A.iter(string):
    print(f"{substr} found at position {end_index - len(substr) + 1}")


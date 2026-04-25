
import ahocorasick

# Define the large string and list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create an Aho-Corasick automaton
automaton = ahocorasick.Automaton()

# Add substrings to the automaton
for index, substring in enumerate(sub_strings):
    automaton.add_word(substring, (index, substring))

# Finalize the automaton
automaton.make_automaton()

# Search for substrings in the large string
for end_index, (index, substring) in automaton.iter(string):
    print(f"{substring} found at position {end_index - len(substring) + 1}")



import ahocorasick

# Create an Aho-Corasick automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for index, substring in enumerate(sub_strings):
    A.add_word(substring, (index, substring))

# Finalize the automaton
A.make_automaton()

# Search through the string
for end_index, (index, substring) in A.iter(string):
    start_index = end_index - len(substring) + 1
    print(substring, start_index)

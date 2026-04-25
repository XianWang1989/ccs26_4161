import ahocorasick

string = "some large text here"
sub_strings = ["some", "text"]

# Create an automaton
A = ahocorasick.Automaton()

# Add all substrings to the automaton
for idx, key in enumerate(sub_strings):
    A.add_word(key, (idx, key))

# Finalize the automaton
A.make_automaton()

# Search for substrings in the main string
for end_index, (idx, word) in A.iter(string):
    start_index = end_index - len(word) + 1
    print(f"{word} found at position {start_index}")

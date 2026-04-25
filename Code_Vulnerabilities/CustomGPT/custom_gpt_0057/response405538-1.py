
from ahocorasick import Automaton
import time

string = "some large text here is some other text that might contain some text"
sub_strings = ["some", "text", "large", "other"]  # Add millions of substrings here

# Initialize the Aho-Corasick automaton
A = Automaton()

# Add the substrings to the automaton
for sub in sub_strings:
    A.add_word(sub, sub)

A.make_automaton()

start_time = time.time()

# Search for the substrings in the larger string
for end_index, original_value in A.iter(string):
    print(f"{original_value} found at index {end_index - len(original_value) + 1}")

end_time = time.time()
print(f"Processing time: {end_time - start_time} seconds")

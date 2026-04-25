
import ahocorasick

def find_substring_positions(larger_string, sub_strings):
    # Create an Aho-Corasick automaton
    A = ahocorasick.Automaton()

    # Add all substrings to the automaton
    for index, substring in enumerate(sub_strings):
        A.add_word(substring, (index, substring))

    # Finalize the automaton
    A.make_automaton()

    positions = {}

    # Search for all substrings in the larger string
    for end_index, (index, substring) in A.iter(larger_string):
        start_index = end_index - len(substring) + 1
        positions[substring] = start_index

    return positions

# Example usage
string = "some large text here"
sub_strings = ["some", "text"]

positions = find_substring_positions(string, sub_strings)
for substring, position in positions.items():
    print(f"{substring} found at position {position}")


import ahocorasick

def find_substrings(large_string, sub_strings):
    # Create an Aho-Corasick Automaton
    A = ahocorasick.Automaton()

    # Add all substrings to the automaton
    for index, substring in enumerate(sub_strings):
        A.add_word(substring, (index, substring))

    # Finalize the automaton
    A.make_automaton()

    # Search for substrings in the large string
    positions = {}
    for end_index, (index, substring) in A.iter(large_string):
        start_index = end_index - len(substring) + 1
        positions[substring] = start_index

    return positions

# Example usage
large_string = "some large text here"
sub_strings = ["some", "text"]
result = find_substrings(large_string, sub_strings)

for substring, position in result.items():
    print(f"'{substring}' found at position {position}")


import ahocorasick

def find_substrings(string, sub_strings):
    # Create an Aho-Corasick Automaton
    A = ahocorasick.Automaton()

    # Add each substring to the automaton
    for idx, sub_string in enumerate(sub_strings):
        A.add_word(sub_string, (idx, sub_string))

    # Finalize the automaton
    A.make_automaton()

    # Search for the substrings in the main string
    positions = {}
    for end_index, (idx, sub_string) in A.iter(string):
        start_index = end_index - len(sub_string) + 1
        positions[sub_string] = start_index

    return positions

# Example usage
string = "some large text here"
sub_strings = ["some", "text", "large", "notfound"]
positions = find_substrings(string, sub_strings)

print(positions)

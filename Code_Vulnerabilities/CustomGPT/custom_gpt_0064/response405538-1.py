
import ahocorasick

# Create an Aho-Corasick automaton
def find_substrings(string, sub_strings):
    # Initialize the automaton
    A = ahocorasick.Automaton()

    # Add each substring to the automaton
    for idx, sub in enumerate(sub_strings):
        A.add_word(sub, (idx, sub))

    # Finalize the automaton
    A.make_automaton()

    # Search for the substrings in the larger string
    results = []
    for end_index, (idx, sub) in A.iter(string):
        start_index = end_index - len(sub) + 1  # Calculate start index
        results.append((sub, start_index))

    return results

# Example usage
string = "some large text here with some text to find"
sub_strings = ["some", "text", "large"]

found_substrings = find_substrings(string, sub_strings)
for sub, pos in found_substrings:
    print(f"{sub} found at position {pos}")


import ahocorasick

# Create an Aho-Corasick automaton
def create_automaton(sub_strings):
    automaton = ahocorasick.Automaton()

    for idx, substring in enumerate(sub_strings):
        automaton.add_word(substring, (idx, substring))

    automaton.make_automaton()
    return automaton

def find_substrings(string, sub_strings):
    results = []
    automaton = create_automaton(sub_strings)

    for end_index, (idx, substring) in automaton.iter(string):
        start_index = end_index - len(substring) + 1
        results.append((substring, start_index))

    return results

# Example usage
string = "some large text here"
sub_strings = ["some", "text"]

found_substrings = find_substrings(string, sub_strings)
for substring, position in found_substrings:
    print(f"{substring} found at position {position}")

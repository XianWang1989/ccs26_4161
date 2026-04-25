
import re

def find_substrings(string, sub_strings):
    # Create an alternation regex from the list of substrings
    regex = re.compile('|'.join(map(re.escape, sub_strings)))

    # Use finditer to get all matches
    for match in regex.finditer(string):
        print(f"{match.group(0)} {match.start()}")

string = "some large text here"
sub_strings = ["some", "text"]
find_substrings(string, sub_strings)

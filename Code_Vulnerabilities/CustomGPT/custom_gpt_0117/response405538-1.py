
import re

# Large string
string = "some large text here" * 1000  # Example to simulate a large string
sub_strings = ["some", "text"]

# Create a pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all occurrences
for match in re.finditer(pattern, string):
    print(f"{match.group()} found at position {match.start()}")


import re

# Your large string
string = "some large text here with some more text to find"
# A list of substrings to search for
sub_strings = ["some", "text", "not_in_string"]

# Creating a regex pattern that matches any substring
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Finding all matches
for match in pattern.finditer(string):
    print(f"{match.group()} found at position {match.start()}")

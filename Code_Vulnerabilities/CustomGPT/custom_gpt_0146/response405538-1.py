
import re

# Define your large string and your list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = "|".join(map(re.escape, sub_strings))

# Use re.finditer to find all occurrences of the pattern in the string
for match in re.finditer(pattern, string):
    print(match.group(), match.start())

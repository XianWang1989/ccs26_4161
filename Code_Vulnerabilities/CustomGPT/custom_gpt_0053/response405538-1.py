
import re

# Define your large string
large_string = "some large text here, some more large text here"
# List of substrings to search
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = "|".join(map(re.escape, sub_strings))

# Use re.finditer to find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, large_string)]

# Print the results
for substr, position in matches:
    print(f"Substring '{substr}' found at position {position}")

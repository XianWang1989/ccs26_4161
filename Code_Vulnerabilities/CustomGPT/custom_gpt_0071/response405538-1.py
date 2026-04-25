
import re

# Define your large string
string = "some large text here with some repeated phrases and other text to check"

# List of substrings to find
sub_strings = ["some", "text", "repeated", "phrases"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches with their positions
matches = [(match.start(), match.group(0)) for match in re.finditer(pattern, string)]

# Display the results
for position, substr in matches:
    print(f"'{substr}' found at position: {position}")

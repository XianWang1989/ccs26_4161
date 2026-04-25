
import re

# Large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text", "large", "example"]  # Add your million substrings here

# Create a single regex pattern
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches with their positions
matches = {match: string.index(match) for match in re.findall(pattern, string)}

# Print matches and their positions
for sub_string, position in matches.items():
    print(f"{sub_string}: {position}")

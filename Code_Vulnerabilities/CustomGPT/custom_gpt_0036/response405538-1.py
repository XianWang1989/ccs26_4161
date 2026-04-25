
import re

# Large string
string = "some large text here with some extra text to check position"
# List of substrings to find
sub_strings = ["some", "text", "extra", "not_in_string"]

# Create a regex pattern that matches all substrings
# The join method creates an or ('|') pattern to match any of the substrings.
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

# Print the substrings and their respective positions
for match in matches:
    print(f"{match.group()} found at position {match.start()}")

# If you want to see the output of not found items, you can loop over sub_strings and check against found items
found_substrings = {match.group(): match.start() for match in matches}
for sub in sub_strings:
    if sub not in found_substrings:
        print(f"{sub} not found")

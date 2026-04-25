
import re

# Sample input string
input_string = "<p>Cash nbs $336,008</p>"

# Regex to match and capture "Cash" and an optional dollar amount
pattern = r"<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?\s*</p>"

# Performing the regex match
match = re.search(pattern, input_string)

if match:
    cash_word = match.group(1)  # Capture group for "Cash"
    dollar_amount = match.group(2)  # Capture group for the dollar amount
    print("Extracted Word:", cash_word)
    print("Extracted Dollar Amount:", dollar_amount if dollar_amount else "None")
else:
    print("No match found.")

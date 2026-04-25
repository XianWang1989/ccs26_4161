
import re

text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>\s*(Cash.*?)?(\$[\d,]+)?\s*</p>"

# Search using the regex pattern
match = re.search(pattern, text)

if match:
    cash_word = match.group(1) if match.group(1) else "Not found"
    amount = match.group(2) if match.group(2) else "Not found"

    print("Word:", cash_word)
    print("Amount:", amount)
else:
    print("No match found.")


import re

# Sample HTML string
html_string = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>\s*(Cash.*?)\s*(\$\d{1,3}(?:,\d{3})*)?\s*</p>"

# Search for matches
match = re.search(pattern, html_string)

if match:
    cash_text = match.group(1)  # "Cash" and following text
    amount = match.group(2)      # The amount, if present
    print(f"Found: '{cash_text}', Amount: '{amount}'")
else:
    print("No match found.")

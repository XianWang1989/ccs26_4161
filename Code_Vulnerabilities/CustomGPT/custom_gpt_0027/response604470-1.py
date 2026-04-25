
import re

text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>\s*(Cash.*?)\s*(\$\d{1,3}(?:,\d{3})*)?\s*</p>"

# Search for matches
matches = re.search(pattern, text)

if matches:
    cash_word = matches.group(1)
    amount = matches.group(2) if matches.group(2) else "No amount found"
    print(f"Extracted text: '{cash_word}'")
    print(f"Extracted amount: '{amount}'")
else:
    print("No match found.")

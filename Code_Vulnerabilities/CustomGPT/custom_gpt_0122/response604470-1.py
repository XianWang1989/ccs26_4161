
import re

# Sample text
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>(.*?\bCash\b.*?)(\$\d{1,3}(?:,\d{3})*)?</p>"

# Search for matches
matches = re.search(pattern, text)

if matches:
    cash_word = matches.group(1).strip()
    amount = matches.group(2) if matches.group(2) else "No amount found"

    print("Extracted word:", cash_word)
    print("Extracted amount:", amount)
else:
    print("No match found.")

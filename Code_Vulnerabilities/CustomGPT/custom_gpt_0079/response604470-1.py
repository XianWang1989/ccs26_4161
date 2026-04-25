
import re

text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>(Cash.*?)\s*(\$\d{1,3}(,\d{3})*)?</p>"

# Search for matches
match = re.search(pattern, text)

if match:
    cash_text = match.group(1)  # captures "Cash and stuff"
    amount = match.group(2)      # captures the dollar amount, if present
    print("Extracted text:", cash_text.strip())
    print("Extracted amount:", amount if amount else "No amount found")
else:
    print("No match found")

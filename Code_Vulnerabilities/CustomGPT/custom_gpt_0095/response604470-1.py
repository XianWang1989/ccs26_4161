
import re

# Sample input string
text = "<p>Cash nbs $336,008</p>"

# Regular expression pattern
pattern = r"<p>(.*?\bCash\b.*?)(\$\d{1,3}(?:,\d{3})*)?</p>"

# Search for matches
match = re.search(pattern, text)

if match:
    cash_word = match.group(1).strip()  # Get the "Cash" part
    cash_amount = match.group(2)         # Get the dollar amount if it exists
    print(f"Found: '{cash_word}'")
    if cash_amount:
        print(f"Amount: {cash_amount}")
else:
    print("No match found.")

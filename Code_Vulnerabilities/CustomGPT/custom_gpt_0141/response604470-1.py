
import re

# Sample input string
text = "<p>Cash nbs $336,008</p>"

# Regular expression to match text inside <p> tags starting with "Cash" and capturing an optional amount
pattern = r"<p>\s*Cash.*?(\$[\d,]+)?\s*</p>"

# Searching for matches
match = re.search(pattern, text)

if match:
    cash_word = "Cash"  # The word 'Cash' is fixed
    amount = match.group(1)  # Capturing the amount if available
    if amount:
        print(f"Extracted: {cash_word} {amount}")
    else:
        print(f"Extracted: {cash_word} (no amount found)")
else:
    print("No match found.")

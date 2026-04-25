
import re

# Sample input
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*|\d+)?\s*</p>"

# Finding matches
match = re.search(pattern, text)

if match:
    cash_word = match.group(1)  # This will capture "Cash"
    amount = match.group(2)      # This will capture the number if present
    print("Cash Word:", cash_word)
    print("Amount:", amount if amount else "No amount found")
else:
    print("No match found")

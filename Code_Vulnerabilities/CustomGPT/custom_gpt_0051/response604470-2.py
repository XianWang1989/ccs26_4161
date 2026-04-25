
import re

text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>(?:Cash.*?(\$\d{1,3}(?:,\d{3})*))?</p>'

# Search for matches
match = re.search(pattern, text)

if match:
    cash_number = match.group(1)  # This captures the dollar amount if available
    print(f"Found 'Cash' and the number is: {cash_number if cash_number else 'Not available'}")
else:
    print("No match found.")

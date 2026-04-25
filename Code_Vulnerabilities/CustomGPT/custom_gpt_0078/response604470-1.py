
import re

text = "<p>Cash nbs $336,008</p>"

# Regex pattern to match the required content
pattern = r'<p>(.*?Cash.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?))<\/p>'

# Search using the regex
match = re.search(pattern, text)

if match:
    cash_text = match.group(0)  # Full match
    cash_amount = match.group(2)  # Only the dollar amount if present
    print(f"Extracted: {cash_text}")
    print(f"Cash Amount: {cash_amount}")
else:
    print("No match found.")

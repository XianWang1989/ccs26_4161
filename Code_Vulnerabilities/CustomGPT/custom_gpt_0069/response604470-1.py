
import re

# Sample HTML input
html = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>(?=.*\bCash\b)(.*?)\$(\d{1,3}(?:,\d{3})*)</p>'

# Search for matches
match = re.search(pattern, html)

if match:
    cash_word = "Cash"
    number = match.group(2) if match.group(2) else "No number found"
    print(f'Found: "{cash_word}" and the number: "${number}"')
else:
    print("No match found.")

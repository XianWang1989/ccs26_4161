
import re

# Sample HTML string
html_string = "<p>Cash nbs $336,008</p>"

# Regex pattern to match "Cash" and an optional number
pattern = r'<p>(.*?)Cash(.*?)\$(\d{1,3}(?:,\d{3})*)<\/p>'

# Search for the pattern
match = re.search(pattern, html_string)

if match:
    cash_word = "Cash"  # Since we are specifically looking for "Cash"
    number = match.group(3) if match.group(3) else None
    print(f'Extracted: {cash_word} {number}')
else:
    print("No match found.")

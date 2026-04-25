
import re

# Sample HTML string
html_string = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Total Sales: $336,008</p>
"""

# Regex pattern
pattern = r'<p>(?=.*\bCash\b)(.*?)(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, html_string)

# Extract and print results
for match in matches:
    cash_word = "Cash" if "Cash" in match[0] else ""
    number = match[1] if match[1] else "No number found"
    print(f'Found: {cash_word}, Number: {number}')

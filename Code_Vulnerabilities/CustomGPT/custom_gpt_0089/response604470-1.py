
import re

# Sample HTML input
html_text = """
<p>Cash nbs $13,000</p>
<p>Total $336,008</p>
<p>Cash some extra text $336,008</p>
"""

# Regular expression to extract "Cash" and optionally a number
pattern = r'<p>.*?\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

# Find all matches
matches = re.findall(pattern, html_text)

# Display the results
for match in matches:
    cash_word = match[0]
    number = match[1] if match[1] else "No number"
    print(f"Found: {cash_word}, Number: {number}")

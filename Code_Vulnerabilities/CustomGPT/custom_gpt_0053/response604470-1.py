
import re

# Sample text
text = """<p>Cash nbs $13,000</p>
<p>Total sales $336,008</p>
<p>Cash amount $336,008</p>"""

# Regex pattern
pattern = r'<p>\s*(Cash).*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and print results
for match in matches:
    cash_word = match[0]  # "Cash"
    number = match[1] if match[1] else "No number found"
    print(f'Found: {cash_word}, Amount: {number}')

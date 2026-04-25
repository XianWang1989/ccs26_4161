
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total expense report $336,008</p>
<p>Random text</p>
"""

# Regex pattern to extract "Cash" and the optional number
pattern = r'<p>\s*(Cash|Total)\s+(?:.*?)(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and display results
for match in matches:
    cash_word = match[0]  # This will be "Cash" or "Total"
    number = match[1] if match[1] else "No number found"
    print(f'Found: "{cash_word}", Number: "{number}"')

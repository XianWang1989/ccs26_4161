
import re

# Example HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Cash some irrelevant text $336,008</p>
<p>Total $500.00</p>
<p>Cash</p>
"""

# Regex pattern to match the desired text inside <p> tags
pattern = r'<p>\s*(Cash)\s.*?(\$[\d{1,3}(?:,\d{3})*|\d]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Print results
for match in matches:
    cash_word = match[0]
    number = match[1] if match[1] else 'N/A'
    print(f"Found: '{cash_word}', Amount: '{number}'")

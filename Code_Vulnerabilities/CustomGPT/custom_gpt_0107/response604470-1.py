
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total revenue: $336,008</p>
"""

# Regex to capture the required information
pattern = r'<p>.*?(Cash)(?:.*?)(\$[\d,]+)?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process and print results
for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else "No amount found"
    print(f'Extracted: {cash_word}, Amount: {amount}')

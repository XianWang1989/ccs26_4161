
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008</p>
<p>Total revenue: $500,000</p>
<p>Cash total $13,000</p>
<p>This is a text without target info.</p>
"""

# Regex pattern
pattern = r'<p>(?=.*\bCash\b)(?:(?!<\/p>).)*(?:\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b)?<\/p>'

# Finding matches
matches = re.findall(pattern, html_content)

# Extract "Cash" and the optional number
for match in matches:
    cash_match = re.search(r'\b(Cash)\b', match)
    number_match = re.search(r'\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b', match)

    cash = cash_match.group(0) if cash_match else None
    number = number_match.group(0) if number_match else None

    print(f'Found: {cash}, Number: {number}')


import re

# Sample HTML string
html_content = """
<p>Cash nbs $336,008</p>
<p>Total nbs $13,000</p>
<p>Cash nbs $13,000</p>
"""

# Regular expression to match "Cash" and an optional number
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Processing matches
result = []
for match in matches:
    cash_word = match[0]
    cash_value = match[1] if match[1] else 'No amount found'
    result.append((cash_word, cash_value))

# Print the results
for cash_word, cash_value in result:
    print(f'Found: "{cash_word}" with amount: "{cash_value}"')


import re

# Sample HTML input
html_input = '''
<p>Cash nbs $13,000</p>
<p>Total sales $336,008</p>
<p>Cash $336,008</p>
'''

# Regex pattern to capture "Cash" and the number
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_input)

# Extract and print the results
for match in matches:
    cash_key = match[0]  # "Cash"
    cash_value = match[1] if match[1] else 'No amount'
    print(f'Key: {cash_key}, Amount: {cash_value}')

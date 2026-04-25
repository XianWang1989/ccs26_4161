
import re

# Your input string
html_string = """
<p>Cash nbs $336,008</p>
<p>Cash nbs $13,000</p>
<p>Something else</p>
<p>Total $100,000</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d{1,3}(,\d{3})*]*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_string)

# Printing the results
for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else 'No amount found'
    print(f'Found: "{cash_word}" with Amount: "{amount}"')

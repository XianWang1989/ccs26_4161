
import re

# Example string with HTML content
text = '''
<p>Cash nbs $13,000</p>
<p>Total expenses $336,008</p>
<p>Cash and some other text $336,008.</p>
'''

# Regex pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Display results
for match in matches:
    cash_word, amount = match
    amount = amount if amount else 'No amount found'
    print(f'Found: {cash_word}, Amount: {amount}')

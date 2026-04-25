
import re

# Sample HTML content
html_content = '''
<p>Cash nbs $336,008</p>
<p>Total nbs $13,000</p>
<p>Cash nbs $13,000</p>
<p>No cash here</p>
'''

# Regex pattern
pattern = r'<p>(.*?Cash.*?)\s*(?:.*?(\$\d{1,3}(?:,\d{3})*))?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process matches
for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else "No amount found"
    print(f"Found: {cash_word}, Amount: {amount}")

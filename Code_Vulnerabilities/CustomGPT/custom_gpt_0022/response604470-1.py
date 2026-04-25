
import re

# Sample text
text = """<p>Cash nbs $336,008</p>
<p>Total nbs $13,000</p>
<p>Cash nbs $13,000</p>"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Print results
for cash, amount in matches:
    print(f"Found: {cash}, Amount: {amount if amount else 'None'}")

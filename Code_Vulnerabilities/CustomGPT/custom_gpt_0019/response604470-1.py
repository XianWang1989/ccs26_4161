
import re

# Sample HTML input
html_content = """
<p>Cash has some stuff nbs $336,008.</p>
<p>Total: $500,000</p>
<p>Cash nbs $13,000</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s.*?\$(\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Display the results
for match in matches:
    cash_word = match[0]  # This will be "Cash"
    amount = match[1]     # This will be the number (if present)
    print(f'Extracted: {cash_word}, Amount: {amount if amount else "No amount found"}')

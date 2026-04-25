
import re

# Example HTML-like string
text = """
<p>Cash nbs $336,008</p>
<p>Total revenue is $13,000</p>
<p>Cash flow is excellent $500,000</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find matches
matches = re.findall(pattern, text)

# Extracting results
results = [(match[0], match[1]) for match in matches]

# Printing results
for cash, amount in results:
    print(f"Found: {cash}, Amount: {amount if amount else 'None'}")

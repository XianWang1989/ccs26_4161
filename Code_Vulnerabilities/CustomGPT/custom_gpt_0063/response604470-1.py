
import re

# Example input
text = """
<p>Cash nbs $13,000</p>
<p>Some text $336,008</p>
<p>Total sales were $250,000</p>
"""

# Regular expression to find text that starts with "Cash"
pattern = r'<p>\s*(Cash)(?:.*?)(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extract and print the results
results = [(match[0], match[1]) for match in matches]
print(results)

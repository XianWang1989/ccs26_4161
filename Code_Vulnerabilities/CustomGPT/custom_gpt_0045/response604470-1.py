
import re

# Example HTML string
html_string = """
<p>Cash nbs $336,008</p>
<p>Cash nbs $13,000</p>
<p>Total nbs $500,000</p>
"""

# Regular expression to match content inside <p> tags and extract the desired text
pattern = r'<p>\s*(Cash).*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_string)

# Process matches to get the desired output
results = [(match[0], match[1]) for match in matches]

# Print the results
for cash, number in results:
    print(f"Found: '{cash}' with number: '{number if number else 'None'}'")

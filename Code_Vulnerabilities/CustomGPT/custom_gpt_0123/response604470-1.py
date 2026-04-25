
import re

text = """
<p>Cash nbs $13,000</p>
<p>Total some text $336,008</p>
<p>Cash additional text $336,008</p>
"""

# Regex to match "Cash" and potentially capture the number
pattern = r"<p>\s*(Cash)\s*.*?\$(\d{1,3}(?:,\d{3})*)\s*</p>"

matches = re.findall(pattern, text)

# Display the results
for match in matches:
    cash, number = match
    print(f"Found: {cash} with number: ${number}")

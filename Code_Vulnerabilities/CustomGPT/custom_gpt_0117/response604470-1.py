
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Some other text $336,008</p>
<p>Total $900.00</p>
"""

# Regular expression pattern
pattern = r'<p>\s*Cash.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extract "Cash" and any dollar amount
results = []
for match in matches:
    results.append(("Cash", match.strip() if match else None))

# Print the results
for result in results:
    print(result)

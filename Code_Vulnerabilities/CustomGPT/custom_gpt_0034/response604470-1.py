
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Total earnings are $500,000</p>
<p>Cash bonus $13,000</p>
"""

# Regular expression pattern
pattern = r'<p>(.*?)Cash.*?(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extracting desired information
results = [(match[0], match[1]) for match in matches]

# Print results
for cash, amount in results:
    print("Found:", cash.strip(), "| Amount:", amount or "None")

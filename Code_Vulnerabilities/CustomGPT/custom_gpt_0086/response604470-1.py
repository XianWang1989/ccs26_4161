
import re

# Sample HTML input
html_content = """
<p>Cash nbs $336,008</p>
<p>Other text</p>
<p>Total nbs $12,000</p>
"""

# Regular expression pattern
pattern = r"<p>.*?(Cash).*?(?:\$([\d,]+))?</p>"

# Find all matches
matches = re.findall(pattern, html_content)

# Process results
results = []
for match in matches:
    cash, amount = match
    if amount:  # if the amount was captured
        results.append((cash, amount))
    else:
        results.append((cash, None))

# Display the results
for cash, amount in results:
    if amount:
        print(f"Found: {cash} with amount {amount}")
    else:
        print(f"Found: {cash} with no amount")

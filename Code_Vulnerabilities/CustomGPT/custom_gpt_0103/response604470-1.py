
import re

# Sample text
text = """
<p>Cash nbs $336,008</p>
<p>Total revenue $432,000</p>
<p>Cash $13,000</p>
"""

# Regex pattern
pattern = r"&lt;p&gt;.*?(Cash).*?(\$[\d,]+)?&lt;\/p&gt;"

# Find all matches
matches = re.findall(pattern, text)

# Extract results
results = []
for match in matches:
    cash_word = match[0]  # "Cash"
    amount = match[1] if match[1] else None  # number or None
    results.append((cash_word, amount))

# Output results
for result in results:
    print(f"Found: {result[0]}, Amount: {result[1]}")

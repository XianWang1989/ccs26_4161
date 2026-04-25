
import re

# Sample text
text = """
<p>Cash nbs $336,008</p>
<p>Total nbs $250,000</p>
<p>Cash nbs $13,000</p>
"""

# Regular expression pattern
pattern = r"<p>.*?(Cash).*?(?:\$\d{1,3}(?:,\d{3})*)?</p>"

# Find all matches
matches = re.findall(pattern, text)

# Extract "Cash" and the corresponding number
results = []
for match in matches:
    cash = match[0]
    number = re.search(r"\$(\d{1,3}(?:,\d{3})*)", match).group(0) if re.search(r"\$(\d{1,3}(?:,\d{3})*)", match) else None
    results.append((cash, number))

# Output results
for cash, number in results:
    print(f"Cash: {cash}, Number: {number if number else 'N/A'}")

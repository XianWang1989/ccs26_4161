
import re

# Sample text containing <p> tags
text = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Total sales are $336,008</p>
<p>Cash has $336,008 and some info</p>
"""

# Regular expression to capture "Cash" and an optional number
pattern = r'<p>.*?(Cash).*?(?:\$([\d,]+))?.*?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and print the results
results = [(match[0], match[1]) for match in matches if match[0]]
for cash, number in results:
    print(f"Found: {cash}, Number: {number if number else 'N/A'}")

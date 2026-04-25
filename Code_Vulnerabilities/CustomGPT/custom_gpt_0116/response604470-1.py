
import re

# Sample text containing <p> tags with cash information
text = """
<p>Cash nbs $13,000</p>
<p>Total expenses $5,000</p>
<p>Cash details: $336,008</p>
"""

# Regex to extract "Cash" and the number if present
pattern = r'<p>.*?Cash.*?(?:\$([\d,]+))?.*?</p>'

# Find all matches in the text
matches = re.findall(pattern, text)

# Process and display results
for match in matches:
    number = match if match else "No number found"
    print(f"Extracted: Cash, Amount: {number}")

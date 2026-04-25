
import re

# Sample text containing <p> tags
text = """
<p>Cash nbs $336,008</p>
<p>Some other text</p>
<p>Total sales $200,000</p>
<p>Cash transaction $13,000</p>
"""

# Regex pattern to find "Cash" and the dollar amount
pattern = r'<p>.*?\b(Cash)\b.*?(\$[\d,]+)?<\/p>'

# Find all matches in the text
matches = re.findall(pattern, text)

# Print the results
for cash, amount in matches:
    print(f"Found: '{cash}'", f"Amount: '{amount}'" if amount else "No amount available")

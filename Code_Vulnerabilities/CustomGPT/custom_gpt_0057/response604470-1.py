
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Total amount $13,000</p>
<p>Cash for next month $13,000</p>
"""

# Regex to find "Cash" and optionally a number
pattern = r'<p>(.*?\bCash\b.*?)?(?:.*?\$(\d{1,3}(?:,\d{3})*)?)<\/p>'

matches = re.findall(pattern, text)

results = []
for match in matches:
    cash_part = match[0] if match[0] else "Cash not found"
    number_part = match[1] if match[1] else "No number found"
    results.append((cash_part.strip(), number_part))

# Displaying results
for cash, number in results:
    print(f'Cash Part: "{cash}", Number: "{number}"')

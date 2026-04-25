
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total amount $336,008</p>
<p>Cash some text $336,008 additional info</p>
"""

# Regex pattern
pattern = r'<p>.*?\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extracting "Cash" and the number if available
results = [(match[0], match[1]) for match in matches]

# Display results
for cash, number in results:
    print(f'Found: "{cash}" with number: "{number if number else "No number found"}"')

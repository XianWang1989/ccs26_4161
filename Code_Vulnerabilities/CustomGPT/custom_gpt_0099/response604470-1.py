
import re

# Sample input string with <p> tags
input_str = """
<p>Cash nbs $13,000</p>
<p>Total $336,008</p>
<p>Some other text</p>
"""

# Regex pattern to match and capture "Cash" and an optional number
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, input_str)

# Displaying the results
for match in matches:
    print(f"Matched: {match[0]}, Amount: {match[1] if match[1] else 'No amount found'}")

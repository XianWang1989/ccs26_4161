
import re

# Sample input string
input_string = """
<p>Cash nbs $336,008</p>
<p>Total revenue $13,000</p>
<p>Other text</p>
"""

# Updated regex pattern
pattern = r'<p>(.*?)Cash.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

# Find all matches
matches = re.findall(pattern, input_string)

# Process matches
for match in matches:
    cash = match[0].strip()  # The text before "Cash"
    number = match[1] if match[1] else "No number found"
    print(f"Found: '{cash}' | Number: '{number}'")

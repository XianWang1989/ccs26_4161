
import re

text = """
<p>Cash nbs $336,008</p>
<p>Cash nbs $13,000</p>
<p>Total: $2,000</p>
<p>Cash</p>
"""

# Regular expression to match "Cash" and the optional number
pattern = r'<p>\s*Cash.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

matches = re.findall(pattern, text)

# Extract and print results
for match in matches:
    print("Cash found", "with number:", match if match else "no number")

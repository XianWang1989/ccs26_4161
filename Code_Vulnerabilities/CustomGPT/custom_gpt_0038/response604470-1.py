
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total revenue for the year $336,008</p>
<p>Cash flow statement $336,008</p>
"""

# Regex pattern to find "Cash" and the optional dollar amount
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Finding all matches
matches = re.findall(pattern, text)

# Displaying the results
for match in matches:
    print("Found:", match[0], "with amount:", match[1] if match[1] else "No amount found")

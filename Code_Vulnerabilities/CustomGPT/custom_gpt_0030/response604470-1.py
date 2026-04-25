
import re

# Sample HTML content
html_content = '''
<p>Cash nbs $13,000</p>
<p>Total income $336,008</p>
<p>Cash follow up $336,008</p>
<p>Other text</p>
'''

# Regular expression to match the desired content
pattern = r'<p>(.*?)Cash.*?(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process the matches to extract required information
result = [(match[0], match[1]) for match in matches if match[1]]

# Print results
for cash, number in result:
    print(f'Found: "{cash.strip()}", Amount: {number.strip()}')


import re

# Sample input string
input_text = """
<p>Cash nbs $336,008</p>
<p>Total amount $12,000</p>
<p>Cash nbs $13,000</p>
"""

# Regular expression to extract content from <p> tags
pattern = r'<p>(.*?)</p>'

# Find all matches
matches = re.findall(pattern, input_text, re.DOTALL)

# Extract "Cash" and the number
for match in matches:
    # Check if 'Cash' is in the match
    if 'Cash' in match:
        # Capture "Cash" and the potential number
        cash_match = re.search(r'Cash.*?(\$\d{1,3}(?:,\d{3})*)?', match)
        if cash_match:
            cash_word = cash_match.group(0).strip()
            number = cash_match.group(1) if cash_match.group(1) else "No number available"
            print(f'Extracted: "{cash_word}" and Number: "{number}"')


import re

# Sample input string
input_text = """
<p>Cash nbs $336,008</p>
<p>Other text</p>
<p>Total: $200</p>
"""

# Regex pattern to capture "Cash" followed by optional content and a number
pattern = r'<p>(.*?)Cash(.*?)\$(\d{1,3}(?:,?\d{3})*)</p>'

# Find all matches in the input_text
matches = re.findall(pattern, input_text)

# Process and print the results
for match in matches:
    cash_phrase = "Cash" + match[1].strip()
    amount = match[2]
    print(f"Found phrase: '{cash_phrase}', Amount: '${amount}'")

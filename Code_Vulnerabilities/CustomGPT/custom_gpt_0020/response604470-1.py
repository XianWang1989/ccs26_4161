
import re

# Sample HTML input
html_content = '''
<p>Cash nbs $13,000</p>
<p>Some other content $500</p>
<p>Cash more text here $336,008</p>
'''

# Pattern to match <p> tags and capture their content
p_pattern = r'<p>(.*?)<\/p>'

# Extract p tag content
p_matches = re.findall(p_pattern, html_content)

# Initialize a list to store the results
results = []

# Loop through each match and apply the second regex
for match in p_matches:
    # Look for "Cash" and the number in the match
    cash_pattern = r'(?i)\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*)?'
    cash_match = re.search(cash_pattern, match)

    if cash_match:
        # Extract 'Cash' and the number if it exists
        cash_word = cash_match.group(1)
        cash_number = cash_match.group(2) if cash_match.group(2) else "Not found"
        results.append((cash_word, cash_number))

# Print the results
for cash_word, cash_number in results:
    print(f'Extracted: {cash_word}, Amount: {cash_number}')

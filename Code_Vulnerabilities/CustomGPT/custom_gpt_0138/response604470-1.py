
import re

text = "<p>Cash nbs $336,008</p>"

# First, find the content inside <p> tags
pattern = r'<p>(.*?)<\/p>'
match = re.search(pattern, text)

if match:
    content = match.group(1)
    # Now search for the word "Cash" and the number
    cash_pattern = r'Cash.*?(\$\d{1,3}(?:,\d{3})*)?'
    cash_match = re.search(cash_pattern, content)

    if cash_match:
        cash = cash_match.group(0)  # This includes "Cash" and the number if present
        number = cash_match.group(1)  # This is only the number if available
        print(f'Extracted: "{cash}"')
        print(f'Number found: "{number}"')
    else:
        print('No match found.')
else:
    print('No <p> tags found.')

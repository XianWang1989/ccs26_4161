
import re

# Sample input string
content = """<p>Cash nbs $13,000</p>"""

# Regex pattern to extract everything in the <p> tags
inner_text_pattern = r'<p>(.*?)<\/p>'
match = re.search(inner_text_pattern, content)

if match:
    inner_text = match.group(1)  # This will give us the text inside <p> tags
    print(f"Text inside <p> tags: {inner_text}")

    # Now let's extract "Cash" and the optional dollar amount
    amount_pattern = r'(Cash).*?(\$\d{1,3}(?:,\d{3})*)?'
    amount_match = re.search(amount_pattern, inner_text)

    if amount_match:
        cash_word = amount_match.group(1)  # "Cash"
        dollar_amount = amount_match.group(2) if amount_match.group(2) else "No amount found"
        print(f"Extracted word: {cash_word}")
        print(f"Extracted amount: {dollar_amount}")
    else:
        print("No match for 'Cash' and amount found.")
else:
    print("No <p> tags found.")

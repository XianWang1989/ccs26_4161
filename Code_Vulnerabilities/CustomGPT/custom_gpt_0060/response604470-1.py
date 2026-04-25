
import re

# Sample text with p tags
text = "<p>Cash nbs $13,000</p>"

# Pattern to capture content inside <p> and </p> tags
# using re.DOTALL to make . match newlines if needed
p_content_pattern = r"<p>(.*?)</p>"

# Find all matches
matches = re.findall(p_content_pattern, text, re.DOTALL)

# Prepare to pull out "Cash" and the number if present
result = []

for match in matches:
    # Use another regex to find "Cash" and the optional number
    cash_pattern = r"(Cash)(?:.*?)(\$[\d,]+)?"
    cash_match = re.search(cash_pattern, match)

    if cash_match:
        # If a match is found, extract the groups
        cash = cash_match.group(1)  # "Cash"
        number = cash_match.group(2) if cash_match.group(2) else None  # Optional number
        result.append((cash, number))

print(result)


import re

# Example string containing <p> tags
text = "<p>Cash nbs $336,008</p><p>Total nbs $13,000</p>"

# Regex pattern explained:
# 1. \<p\> - Matches the opening <p> tag.
# 2. (Cash) - Captures the word "Cash".
# 3. .*? - Matches any text non-greedily until the number.
# 4. (\$[\d,]+) - Captures the dollar amount (with optional commas).
# 5. \<\/p\> - Matches the closing </p> tag.

pattern = r"<p>(Cash.*?)\$([\d,]+)</p>"

# Perform the regex search
matches = re.findall(pattern, text)

# Process the matches
for match in matches:
    cash_word = match[0].strip()  # Will contain "Cash" and potentially some unwanted text
    amount = match[1] if match[1] else None  # Will contain the dollar amount if available
    print("Cash Word:", cash_word)
    print("Amount:", amount)

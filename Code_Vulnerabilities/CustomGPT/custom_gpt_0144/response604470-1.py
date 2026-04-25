import re

# Sample text input
html_content = '''
<p>begins with the word "Cash" has some stuff I don't want then a number $336,008.</p>
<p>From:</p>
<blockquote>
  <p><code>&lt;p&gt;Cash nbs $13,000&lt;/p&gt;</code></p>
</blockquote>
'''

# Step 1: Extract the content inside <p> tags
p_tag_pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
p_tag_matches = p_tag_pattern.findall(html_content)

# Step 2: Search for "Cash" and optionally the number
cash_pattern = re.compile(r'Cash.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?', re.DOTALL)

# Find the matches
for match in p_tag_matches:
    cash_match = cash_pattern.search(match)
    if cash_match:
        # Extract "Cash" and the number (if available)
        print("Found:", cash_match.group(0))
        print("Cash:", cash_match.group(0).split()[0])
        if cash_match.group(1):
            print("Amount:", cash_match.group(1))
        else:
            print("Amount: Not available")

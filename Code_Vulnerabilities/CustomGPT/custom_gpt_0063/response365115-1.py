
import re

# Example plot string with multiple placeholders
plot = "This is a _choice1_ and here is _choice2_. Again, _choice1_ appears."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Function to replace placeholders
def substitute_choices(match):
    if match.group(0) == '_choice1_':
        return data1
    elif match.group(0) == '_choice2_':
        return data2

# Substitute all occurrences of _choice1_ and _choice2_
plot = re.sub(r'_choice1_|_choice2_', substitute_choices, plot)

print(plot)

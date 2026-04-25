
import re

# Sample plot string
plot = "This is a test: _choice1_ and _choice2_ and _choice1_."

# Data for substitution
data1 = "Option 1"
data2 = "Option 2"

# Function to handle substitutions
def substitute_choice(match):
    if match.group(0) == '_choice1_':
        return data1
    elif match.group(0) == '_choice2_':
        return data2

# Use re.sub with the function
plot = re.sub(r'_choice1_|_choice2_', substitute_choice, plot)

print(plot)

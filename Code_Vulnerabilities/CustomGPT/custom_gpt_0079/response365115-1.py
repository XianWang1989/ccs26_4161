
import re

# Example data
plot = "This is a plot with _choice1_ and _choice2_."
data1 = "Option A"
data2 = "Option B"

# Dictionary for substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Function to perform the replacement
def substitute(match):
    return substitutions[match.group(0)]

# Use re.sub with a function
plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)

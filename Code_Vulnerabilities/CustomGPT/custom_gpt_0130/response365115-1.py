
import re

data1 = "value1"
data2 = "value2"

# Example plot string
plot = "This is a _choice1_ and here is _choice2_. _choice1_ again."

# Create a mapping for substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Substitute using a function
def substitute(match):
    return substitutions[match.group(0)]

# Perform the substitution
plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)

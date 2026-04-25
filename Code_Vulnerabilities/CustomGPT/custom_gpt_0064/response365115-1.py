
import re

# Sample input
plot = "This is a _choice1_ and here is another _choice2_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Create a dictionary for substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Substitute using a function
def substitute(match):
    return substitutions[match.group(0)]

# Perform the substitution
pattern = re.compile('|'.join(re.escape(key) for key in substitutions.keys()))
plot = pattern.sub(substitute, plot)

print(plot)  # Output: This is a option A and here is another option B.

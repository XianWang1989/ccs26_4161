
import re

# Sample data
data1 = "value1"
data2 = "value2"

# Sample plot string with multiple placeholders
plot = "This is a test with _choice1_ and another _choice1_ and _choice2_."

# Use a dictionary for substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2,
}

# Function to substitute using the dictionary
def substitute_placeholders(match):
    return substitutions[match.group(0)]

# Perform the substitution
pattern = re.compile('|'.join(re.escape(key) for key in substitutions.keys()))
plot = pattern.sub(substitute_placeholders, plot)

print(plot)

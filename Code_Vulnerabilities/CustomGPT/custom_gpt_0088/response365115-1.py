
import re

# Sample data
plot = "This is a _choice1_ and this is another _choice1_ and also a _choice2_."
data1 = "first choice"
data2 = "second choice"

# Dictionary to hold substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2,
}

# Substitute using a function
def replace(match):
    return substitutions[match.group(0)]

# Perform substitution
plot = re.sub(r'_choice1_|_choice2_', replace, plot)

print(plot)

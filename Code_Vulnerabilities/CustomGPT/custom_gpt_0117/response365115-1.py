
import re

# Example data
data1 = "Data for choice 1"
data2 = "Data for choice 2"
plot = "This is a plot with _choice1_ and _choice2_"

# Create a dictionary with substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Function to substitute placeholders
def substitute(match):
    return substitutions[match.group(0)]

# Substitute using re.sub with the function
plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)

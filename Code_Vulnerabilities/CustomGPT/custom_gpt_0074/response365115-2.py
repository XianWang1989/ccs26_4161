
import re

data1 = "Value1"
data2 = "Value2"
plot = "This is a test string with _choice1_ and _choice2_ and also _choice1_ again."

# Create a dictionary of substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# A function to replace based on the dictionary
def substitute(match):
    return substitutions[match.group(0)]

# Use re.sub with a pattern
plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)

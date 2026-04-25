
import re

# Sample data
data1 = "Value1"
data2 = "Value2"
plot = "_choice1_ and then _choice2_ happened, followed by _choice1_ again."

# You can define a dictionary for substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# A function to perform the substitutions
def substitute_choices(match):
    return substitutions[match.group(0)]

# Use re.sub with a function
plot = re.sub(r'_choice1_|_choice2_', substitute_choices, plot)

print(plot)

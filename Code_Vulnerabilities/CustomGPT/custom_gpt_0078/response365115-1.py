
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice2_."
data1 = "apple"
data2 = "orange"

# Create a dictionary for substitutions
data = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Use a function to substitute all occurrences
def substitute(match):
    return data[match.group(0)]

# Substitute all occurrences
plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)


import re

# Example plot template
plot = "This is a _choice1_ and that is a _choice2_."

# Variables to substitute
data1 = "sample data 1"
data2 = "sample data 2"

# Perform substitutions
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

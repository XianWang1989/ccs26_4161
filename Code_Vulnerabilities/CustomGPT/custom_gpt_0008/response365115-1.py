
import re

# Example data
plot = "This is a _choice1_ and another _choice1_ and also a _choice2_."
data1 = "option A"
data2 = "option B"

# Use re.sub with a lambda function for substitution
plot = re.sub(r'_choice1_', lambda x: data1, plot)
plot = re.sub(r'_choice2_', lambda x: data2, plot)

print(plot)

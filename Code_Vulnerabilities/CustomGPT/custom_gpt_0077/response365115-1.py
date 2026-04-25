
import re

# Sample string
plot = "This is a _choice1_ and another _choice2_. And here is _choice1_ again!"

# Data for substitution
data1 = "apple"
data2 = "orange"

# Substitute using re.sub
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use str.format to fill in the variables
result = plot % (data1, data2)
print(result)

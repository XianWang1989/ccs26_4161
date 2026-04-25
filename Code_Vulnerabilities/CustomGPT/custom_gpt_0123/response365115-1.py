
import re

# Sample plot text with placeholders
plot = "This is a _choice1_ and another _choice1_. Also, here is a _choice2_."

# Data for substitution
data1 = "apple"
data2 = "banana"

# Substitute all occurrences using re.sub
plot = re.sub(r'_choice1_', '%s', plot) % (data1,)  # Use a tuple for single value
plot = re.sub(r'_choice2_', '%s', plot) % (data2,)  # Use a tuple for single value

print(plot)

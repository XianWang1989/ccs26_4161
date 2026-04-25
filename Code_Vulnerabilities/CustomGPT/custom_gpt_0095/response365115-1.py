
import re

# Sample plot string
plot = "This is a _choice1_ and also a _choice2_ and another _choice1_."

# Data for substitution
data1 = "apple"
data2 = "banana"

# Substitute using re.sub
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)

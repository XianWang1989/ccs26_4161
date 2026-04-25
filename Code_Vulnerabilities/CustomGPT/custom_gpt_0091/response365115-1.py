
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and that is a _choice2_. Also, another _choice1_."

# Data to substitute
data1 = "option1"
data2 = "option2"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use % formatting with a tuple of values
plot = plot % (data1, data2)

print(plot)

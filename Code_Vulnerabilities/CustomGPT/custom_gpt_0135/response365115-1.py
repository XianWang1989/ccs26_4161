
import re

# Sample plot string with variables
plot = "This is a _choice1_ and another _choice1_ with a _choice2_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Replace using str.format
plot = plot % (data1, data2)

print(plot)

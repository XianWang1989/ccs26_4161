
import re

# Sample plot string
plot = "This is a _choice1_ and then another _choice1_ and _choice2_."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Substitute variables using re.sub directly with format strings
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

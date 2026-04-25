
import re

# Sample string
plot = "This is a _choice1_ and this is another _choice1_ and _choice2_."

# Example data
data1 = "Option A"
data2 = "Option B"

# Substitutes for all occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)

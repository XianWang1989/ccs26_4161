
import re

# Sample data
plot = "This is _choice1_ and this is also _choice2_ and _choice1_."
data1 = "Option A"
data2 = "Option B"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)


import re

# Sample plot string with multiple occurrences of placeholders
plot = "This is a _choice1_ and another _choice1_ along with a _choice2_."

# Sample data
data1 = "Option A"
data2 = "Option B"

# Use re.sub to substitute all occurrences
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

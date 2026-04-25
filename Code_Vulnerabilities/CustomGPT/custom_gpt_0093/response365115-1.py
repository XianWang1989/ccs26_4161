
import re

# Sample plot string
plot = "This is a _choice1_ and another _choice1_, also here is _choice2_."

# Data for substitution
data1 = "Option A"
data2 = "Option B"

# Replace occurrences
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

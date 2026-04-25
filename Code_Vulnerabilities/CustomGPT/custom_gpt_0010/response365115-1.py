
import re

# Sample data
plot = "This is a _choice1_ text with _choice1_ and _choice2_."

# Data for substitution
data1 = "Option A"
data2 = "Option B"

# Replacing multiple occurrences correctly
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)

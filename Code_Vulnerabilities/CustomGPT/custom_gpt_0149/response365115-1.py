
import re

# Sample plot string
plot = "This is _choice1_ and also _choice1_ and _choice2_."

# Data to substitute
data1 = "option1"
data2 = "option2"

# Substitute all occurrences
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

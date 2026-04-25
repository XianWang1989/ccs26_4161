
import re

# Example plot string
plot = "This is a plot with _choice1_ and _choice1_ and also _choice2_."

# Data to substitute in
data1 = "first_choice"
data2 = "second_choice"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot) % (data1,)
plot = re.sub(r'_choice2_', '%s', plot) % (data2,)

print(plot)

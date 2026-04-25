
import re

# Sample data
plot = "This is a _choice1_ plot and here is another _choice1_ along with _choice2_."
data1 = "example1"
data2 = "example2"

# Substitute all occurrences of the placeholders
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

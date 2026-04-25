
import re

# Sample data
plot = "This is a _choice1_ and another _choice1_ and here is _choice2_."

# Data for substitution
data1 = "Apple"
data2 = "Banana"

# Substitute occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)


import re

data1 = "value1"
data2 = "value2"
plot = "This is a _choice1_ and also a _choice1_ and this is _choice2_."

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)


import re

# Example variables
data1 = "value1"
data2 = "value2"
plot = "_choice1_ some text _choice2_ more text _choice1_"

# Substitute and format in a safe way
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)


import re

# Example variables
data1 = "Value1"
data2 = "Value2"

# Sample plot string with placeholders
plot = "_choice1_ and _choice2_ are your options. Choose _choice1_ again!"

# Substitute placeholders with values
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

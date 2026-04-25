
import re

# Example data
data1 = "Option A"
data2 = "Option B"
plot = "Please select: _choice1_ and _choice2_ for your options. _choice1_ is important."

# Substitute variables
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

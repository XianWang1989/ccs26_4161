
import re

# Sample data
plot = "This is a _choice1_ and that is _choice2_ and again _choice1_."
data1 = "Option A"
data2 = "Option B"

# Substitute using re.sub
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with the replaced values
plot = plot.format(data1, data2)

print(plot)

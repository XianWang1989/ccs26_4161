
import re

# Example initial plot string with placeholders
plot = "This is a test _choice1_ and here is _choice2_. Let's see _choice1_ again."

# Data to substitute
data1 = "Data for choice 1"
data2 = "Data for choice 2"

# Perform substitutions
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the plot string with the data
plot = plot.format(data1, data2)

# Output the final plot string
print(plot)


import re

# Sample plot string with placeholders
plot = "This is a test with _choice1_ and _choice2_. Let's see _choice1_ again."

# Data that will replace the placeholders
data1 = "option A"
data2 = "option B"

# Use re.sub for both variable substitutions
# Use a single format string to replace the chosen names
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now you can format the plot string with both data
formatted_plot = plot % (data1, data2)

print(formatted_plot)

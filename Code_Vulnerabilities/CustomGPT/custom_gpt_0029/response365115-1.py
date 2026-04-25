
import re

# Sample data
data1 = "value1"
data2 = "value2"
plot = "_choice1_ and _choice2_ and _choice1_ again."

# Perform substitutions
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Use str.format to fill the placeholders
final_plot = plot.format(data1, data2)

print(final_plot)

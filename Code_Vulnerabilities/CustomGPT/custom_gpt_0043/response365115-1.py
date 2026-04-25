
import re

# Sample plot string with multiple occurrences of placeholders
plot = "This is a _choice1_ text with _choice1_ and _choice2_ appearances."

# Data to substitute into the plot
data1 = "first choice"
data2 = "second choice"

# Substituting multiple occurrences
# Using a function to perform the substitutions
plot = plot.replace('_choice1_', '%s' % data1)  # Replace first choice
plot = plot.replace('_choice2_', data2)          # Replace second choice

print(plot)

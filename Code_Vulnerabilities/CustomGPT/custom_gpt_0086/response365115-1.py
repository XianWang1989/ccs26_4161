
import re

# Sample plot string with multiple placeholders
plot = "Here is _choice1_ and here is _choice1_ again. Also, _choice2_ is here."

# Data for substitution
data1 = "Apple"
data2 = "Banana"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the plot with the data
plot = plot % (data1, data1, data2)  # Provide data according to placeholders

print(plot)

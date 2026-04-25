
import re

# Sample plot string with multiple occurrences
plot = "This is a test with _choice1_ and _choice1_ again and _choice2_."

# Data to substitute
data1 = "First Choice"
data2 = "Second Choice"

# Substitute all occurrences using re.sub
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with data
plot = plot.format(data1, data2)

print(plot)

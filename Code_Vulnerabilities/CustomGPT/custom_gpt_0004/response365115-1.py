
import re

plot = "Sample with _choice1_ and another _choice1_ and _choice2_"
data1 = "first_choice"
data2 = "second_choice"

# Substitute placeholders with format
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Use str.format to replace placeholders
plot = plot.format(data1, data2)

print(plot)

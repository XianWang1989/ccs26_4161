
import re

# Sample plot string
plot = "This is a _choice1_ and this is another _choice1_ and also a _choice2_."

# Example data
data1 = "first choice"
data2 = "second choice"

# Substitute placeholders and format using .format()
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Final formatted string
plot = plot.format(data1, data2)

print(plot)

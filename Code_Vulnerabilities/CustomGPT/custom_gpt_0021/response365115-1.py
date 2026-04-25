
import re

# Example data
plot = "This is a plot with _choice1_ and another _choice1_ and also _choice2_."
data1 = "first choice"
data2 = "second choice"

# Use str.format for substitution
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with the data
formatted_plot = plot.format(data1, data2)
print(formatted_plot)

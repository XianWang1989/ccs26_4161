
import re

# Your plot string with placeholders
plot = "This is a _choice1_ and that is a _choice2_. Repeating _choice1_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Use re.sub to substitute placeholders
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the plot with the data
formatted_plot = plot % (data1, data2)
print(formatted_plot)


import re

# Sample data
data1 = "Apple"
data2 = "Banana"
plot = "This is a plot with _choice1_ and _choice2_. _choice1_ is also here."

# Use re.sub to replace placeholders
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with both data values
formatted_plot = plot % (data1, data2)

print(formatted_plot)

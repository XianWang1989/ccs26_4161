
import re

# Sample data
plot = "_choice1_ and _choice2_ are options."
data1 = "Option 1"
data2 = "Option 2"

# Use re.sub for substitutions and format the result:
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now safely format once, using a tuple for multiple substitutions
formatted_plot = plot % (data1, data2)

print(formatted_plot)

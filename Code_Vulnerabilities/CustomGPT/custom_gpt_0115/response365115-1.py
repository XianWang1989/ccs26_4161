
import re

# Sample data and plot string
data1 = 'Apple'
data2 = 'Banana'
plot = "I like _choice1_ and _choice2_. Also, _choice1_ is my favorite."

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with data
plot = plot % (data1, data2)

print(plot)

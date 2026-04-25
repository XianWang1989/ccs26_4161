
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_ and also _choice2_."
data1 = "option A"
data2 = "option B"

# Substitute using re.sub
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the plot string with the data
plot = plot % (data1, data2)

print(plot)

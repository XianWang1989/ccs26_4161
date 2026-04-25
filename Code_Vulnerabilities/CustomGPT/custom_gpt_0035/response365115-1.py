
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice2_ and yet another _choice1_."
data1 = "first"
data2 = "second"

# Substitute choices with formatted strings
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Ensure correct data substitution
plot = plot % (data1, data2)

print(plot)

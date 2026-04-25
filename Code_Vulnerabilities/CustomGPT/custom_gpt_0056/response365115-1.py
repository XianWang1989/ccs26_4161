
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_. Then there's _choice2_."
data1 = "apple"
data2 = "banana"

# Perform substitutions
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

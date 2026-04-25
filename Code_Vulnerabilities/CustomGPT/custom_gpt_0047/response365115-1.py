
import re

# Sample data
plot = "This is a _choice1_ and this is another _choice1_ and a _choice2_."
data1 = "apple"
data2 = "banana"

# Use re.sub to substitute placeholders
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with the data
plot = plot.format(data1, data2)

print(plot)

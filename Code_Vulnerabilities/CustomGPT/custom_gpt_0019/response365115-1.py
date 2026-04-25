
import re

# Sample data
data1 = "value1"
data2 = "value2"
plot = "This is a _choice1_ and here is another _choice1_. Then we have _choice2_."

# Substitute placeholders with formatted values
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use the format method to substitute values
plot = plot % (data1, data1, data2)

print(plot)

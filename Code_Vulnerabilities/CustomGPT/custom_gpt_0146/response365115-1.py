
import re

data1 = "Value1"
data2 = "Value2"
plot = "This is a string with _choice1_ and _choice2_ in it. _choice1_ appears again."

# Using re.sub to replace placeholders with {} to use str.format
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Now formatting the string
plot = plot.format(data1, data2)

print(plot)

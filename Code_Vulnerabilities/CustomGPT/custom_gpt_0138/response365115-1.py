
import re

# Sample plot string
plot = "This is a _choice1_ and this is another _choice1_ and more _choice2_."

# Data to substitute
data1 = "apple"
data2 = "banana"

# Substitute occurrences
plot = plot.replace('_choice1_', data1).replace('_choice2_', data2)

print(plot)

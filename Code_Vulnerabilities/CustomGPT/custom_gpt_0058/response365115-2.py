
import re

# Sample plot string
plot = "This is a _choice1_ and another _choice2_ _choice1_."

# Data to substitute
data1 = "apple"
data2 = "banana"

# Using re.sub and f-string formatting
plot = re.sub(r'_choice1_', f'{data1}', plot)
plot = re.sub(r'_choice2_', f'{data2}', plot)

# Printing the result
print(plot)

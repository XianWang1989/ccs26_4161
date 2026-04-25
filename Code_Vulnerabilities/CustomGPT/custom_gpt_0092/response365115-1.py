
import re

# Sample plot string
plot = "This is a test _choice1_ and another _choice2_ for _choice1_."

# Data to substitute
data1 = "option1"
data2 = "option2"

# Substitute using a tuple for multiple occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Final formatting with all substitutions
plot = plot % (data1, data2)

print(plot)

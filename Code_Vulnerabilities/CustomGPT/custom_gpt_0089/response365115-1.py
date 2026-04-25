
import re

# Example plot string with placeholders
plot = "This is a _choice1_ and here is another _choice1_. Also, _choice2_ is present."

# Data for substitution
data1 = "option A"
data2 = "option B"

# Using re.sub for substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Using % operator to substitute values
plot = plot % (data1, data1, data2)

print(plot)

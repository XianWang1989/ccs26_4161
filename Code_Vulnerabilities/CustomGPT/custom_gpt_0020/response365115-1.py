
import re

# Example plot string with placeholders
plot = "This is a _choice1_ and another _choice1_ and also _choice2_"

# Data to substitute
data1 = 'Apple'
data2 = 'Banana'

# Substitute the placeholders in the plot
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now apply the substitutions with the tuple of replacements
plot = plot % (data1, data1, data2)

print(plot)

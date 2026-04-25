
import re

# Your data
data1 = "First choice"
data2 = "Second choice"
plot = "This is a _choice1_ and this is another _choice1_ and here is _choice2_."

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now use % formatting correctly
plot = plot % (data1, data2)

print(plot)

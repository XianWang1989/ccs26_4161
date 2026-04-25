
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_ and a _choice2_."
data1 = "first choice"
data2 = "second choice"

# Substitute placeholders with a format function
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

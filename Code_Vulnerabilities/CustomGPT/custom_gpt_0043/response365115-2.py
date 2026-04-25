
import re

plot = "This is a _choice1_ text with _choice1_ and _choice2_ appearances."
data1 = "first choice"
data2 = "second choice"

# Using re.sub to replace placeholders
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

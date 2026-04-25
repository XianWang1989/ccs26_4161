
import re

plot = "Here is some text with _choice1_ and again _choice1_, and also _choice2_."
data1 = "first choice"
data2 = "second choice"

# Use re.sub to perform the replacements
plot = re.sub(r'_choice1_', '{}', plot)  # Substitute with a placeholder for choice1
plot = re.sub(r'_choice2_', '{}', plot)  # Substitute with a placeholder for choice2

# Now use str.format to fill the placeholders
plot = plot.format(data1, data2)

print(plot)

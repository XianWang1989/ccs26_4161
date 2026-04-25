
import re

# Sample string
plot = "This is the _choice1_ text and this is another _choice1_ and _choice2_."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Final formatting
final_plot = plot % (data1, data2)

print(final_plot)

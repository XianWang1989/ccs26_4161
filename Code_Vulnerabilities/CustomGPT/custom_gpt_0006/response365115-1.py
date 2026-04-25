
import re

# Sample data and plot string
data1 = "First"
data2 = "Second"
plot = "This is a _choice1_ and this is a _choice2_. _choice1_ again."

# Substitute placeholders using re.sub
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the final string with data
final_plot = plot % (data1, data2)

print(final_plot)

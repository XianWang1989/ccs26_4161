
import re

# Example data
plot = "This is _choice1_ and this is _choice2_."
data1 = "first choice"
data2 = "second choice"

# Substitute using re.sub for multiple occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with the data variables
formatted_plot = plot % (data1, data2)

print(formatted_plot)  # Outputs: This is first choice and this is second choice.

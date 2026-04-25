
import re

# Sample plot string with placeholders
plot = "This is a sample _choice1_ and another _choice2_ example with _choice1_ again."

# Data to substitute
data1 = "option1"
data2 = "option2"

# Substitute placeholders using re.sub
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with the corresponding data
plot = plot % (data1, data2)

print(plot)

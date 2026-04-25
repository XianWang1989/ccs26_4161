
import re

# Sample string with multiple occurrences
plot = "This is a _choice1_ test. Another _choice1_ occurs here. Also, _choice2_ is present."

# Data to substitute
data1 = "option1"
data2 = "option2"

# Perform substitution safely
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

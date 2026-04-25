
import re

data1 = "Value1"
data2 = "Value2"
plot = "This is a test string with _choice1_ and _choice2_ and also _choice1_ again."

# Substitute the placeholders with formatting
plot = re.sub(r'_choice1_', '%s', plot) % (data1,)
plot = re.sub(r'_choice2_', '%s', plot) % (data2,)

print(plot)

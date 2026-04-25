
import re

# Sample data
data1 = "First Choice"
data2 = "Second Choice"
plot = "This is a _choice1_ and this is a _choice2_"

# Substitute using re.sub with a lambda function
plot = re.sub(r'_choice1_', lambda match: "%s" % data1, plot)
plot = re.sub(r'_choice2_', lambda match: "%s" % data2, plot)

print(plot)

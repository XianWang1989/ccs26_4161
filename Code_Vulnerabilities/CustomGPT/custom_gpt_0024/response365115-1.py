
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and another _choice1_ along with _choice2_."

# Data for substitution
data1 = "first choice"
data2 = "second choice"

# Use re.sub with a lambda function to substitute multiple occurrences
plot = re.sub(r'_choice1_|_choice2_', 
               lambda match: data1 if match.group(0) == '_choice1_' else data2, 
               plot)

print(plot)

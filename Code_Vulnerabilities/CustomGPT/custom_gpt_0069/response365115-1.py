
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice2_ in the text."
data1 = "apple"
data2 = "orange"

# Using a dictionary to hold your substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

# Perform substitutions
for key, value in substitutions.items():
    plot = re.sub(re.escape(key), value, plot)

print(plot)

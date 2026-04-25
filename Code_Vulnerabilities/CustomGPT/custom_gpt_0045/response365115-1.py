
import re

# Example plot string
plot = "This is a sample plot with _choice1_ and _choice2_. Also _choice1_ again."

# Data to replace the placeholders
data1 = "option A"
data2 = "option B"

# Using a loop to handle multiple substitutions
substitutions = {
    '_choice1_': data1,
    '_choice2_': data2
}

for placeholder, replacement in substitutions.items():
    plot = re.sub(re.escape(placeholder), replacement, plot)

print(plot)


import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and this is a _choice2_."

# Data to substitute
data = {
    '_choice1_': 'apple',
    '_choice2_': 'orange'
}

# Substitute all occurrences
for key, value in data.items():
    plot = re.sub(re.escape(key), value, plot)

print(plot)

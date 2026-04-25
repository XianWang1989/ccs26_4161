
import re

# Sample plot string
plot = "This is a _choice1_ and this is another _choice1_ and more _choice2_."

# Data to substitute
data1 = "apple"
data2 = "banana"

# Use a dictionary for substitution
replacements = {
    '_choice1_': data1,
    '_choice2_': data2,
}

# Substitute occurrences
pattern = re.compile('|'.join(re.escape(key) for key in replacements.keys()))

def replacement(match):
    return replacements[match.group(0)]

plot = pattern.sub(replacement, plot)

print(plot)

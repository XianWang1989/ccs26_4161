
import re

# Sample plot string with placeholders
plot = "This is a plot with _choice1_ and _choice2_, and again _choice1_."

# Values to substitute
data1 = "Option1"
data2 = "Option2"

# Substitute using regex
plot = plot.replace("_choice1_", data1).replace("_choice2_", data2)

print(plot)

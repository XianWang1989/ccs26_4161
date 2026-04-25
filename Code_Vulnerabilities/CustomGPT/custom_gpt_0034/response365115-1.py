
import re

# Sample plot string
plot = "This is a sample plot with _choice1_ and _choice2_ included."

# Data to substitute
data1 = "Option A"
data2 = "Option B"

# Substitute and format
plot = plot.replace('_choice1_', '{}').replace('_choice2_', '{}').format(data1, data2)

print(plot)

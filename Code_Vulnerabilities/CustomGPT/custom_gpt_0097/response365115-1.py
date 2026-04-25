
import re

plot = "This is _choice1_ and here is _choice2_. _choice1_ again!"

data1 = "Option 1"
data2 = "Option 2"

plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)

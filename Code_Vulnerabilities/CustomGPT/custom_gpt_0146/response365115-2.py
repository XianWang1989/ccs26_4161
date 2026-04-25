
import re

data1 = "Value1"
data2 = "Value2"
plot = "This is a string with _choice1_ and _choice2_ in it. _choice1_ appears again."

# Using re.sub to replace placeholders with an f-string style
plot = re.sub(r'_choice1_', f'{data1}', plot)
plot = re.sub(r'_choice2_', f'{data2}', plot)

print(plot)

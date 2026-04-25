
import re

data = {
    '_choice1_': "First Choice",
    '_choice2_': "Second Choice"
}
plot = "This is a plot with _choice1_ and _choice2_."

for key, value in data.items():
    plot = re.sub(re.escape(key), value, plot)

print(plot)

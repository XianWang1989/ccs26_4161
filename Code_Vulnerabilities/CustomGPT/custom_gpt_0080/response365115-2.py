
plot = "_choice1_ is chosen, and _choice2_ is also selected."
data1 = "Option A"
data2 = "Option B"

# Using str.format
plot = plot.replace('_choice1_', data1).replace('_choice2_', data2)

print(plot)


# Use a dictionary for clarity
data = {
    'choice1': data1,
    'choice2': data2
}

# Substitute and format
plot = "This is a _choice1_ and another _choice1_ with a _choice2_."
for key, value in data.items():
    plot = plot.replace(f'_{key}_', value)

print(plot)

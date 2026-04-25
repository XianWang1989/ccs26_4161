
# Open the file using 'with' to ensure proper closure
with open('reg.fa', 'r') as fh:
    # Read line by line to save memory
    lines = []
    for line in fh:
        # Remove newline characters and append to the list
        lines.append(line.strip())

# Join lines into a single string if needed
s = ''.join(lines)

# Print the result
print(s)

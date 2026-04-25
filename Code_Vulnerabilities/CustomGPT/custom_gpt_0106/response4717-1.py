
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Use a list to collect lines
    lines = []

    # Read the file line by line
    for line in fh:
        # Remove newline characters and store the lines
        lines.append(line.strip())

# Join lines if needed
result = ''.join(lines)

# Print the final result
print(result)

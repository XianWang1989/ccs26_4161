
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the modified lines
    s = ''

    # Read file line by line
    for line in fh:
        # Remove newline characters and accumulate the result
        s += line.strip()

# Print the final string without newlines
print(s)

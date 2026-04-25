
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the output
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and append to the string
        s += line.strip()

# Print the result
print(s)

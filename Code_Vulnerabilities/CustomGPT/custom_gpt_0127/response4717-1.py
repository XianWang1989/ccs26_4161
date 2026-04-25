
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate lines
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and accumulate
        s += line.strip()

# Print the resulting string
print(s)


# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the contents
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and append to the string
        s += line.strip()

# Now 's' contains all the content without newlines
print(s)

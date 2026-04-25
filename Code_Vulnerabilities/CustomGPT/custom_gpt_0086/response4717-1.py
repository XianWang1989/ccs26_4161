
# Open the file using a context manager to ensure proper handling
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters from the line and add to the string
        s += line.strip()

# Print the concatenated result
print(s)

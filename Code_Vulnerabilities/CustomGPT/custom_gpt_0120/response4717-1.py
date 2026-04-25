
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove the newline character
        s += line.strip()  # This will also concatenate the lines

# Print the final string without newlines
print(s)

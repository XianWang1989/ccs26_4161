
# Open the file in read mode using 'with' to ensure proper resource management
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Clean line by removing newline characters
        line = line.strip()
        # Concatenate the cleaned line to the string (if needed)
        s += line

# Now, s contains the content of the file without newlines
print(s)

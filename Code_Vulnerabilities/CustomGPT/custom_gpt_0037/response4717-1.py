
# Open the file using a context manager
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and concatenate to s
        s += line.strip()  # Use strip() instead of replace() for efficiency

# Now you can work with the final string s without newlines
print(s)

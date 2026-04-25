
# Open the file using a context manager for better resource management
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store processed lines
    s = ''

    # Iterate through each line in the file
    for line in fh:
        # Remove newline characters and append to the string
        s += line.strip()

# Print the final string
print(s)


# Open the file using 'with' to ensure it's properly closed
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for storing contents
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove the newline character and update the string
        s += line.strip()

# Print the final string without any newline characters
print(s)


# Efficient file handling for large files
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store content
    s = ''

    # Read file line by line
    for line in fh:
        # Remove newline characters and append the line to the string
        s += line.strip()  # Using strip() to remove leading/trailing whitespace

# Print the final result
print(s)

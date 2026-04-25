
# Open the file using a context manager for proper resource management
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    result = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters
        result += line.strip()  # Use strip() to remove whitespace/newlines

# Print the resultant string
print(result)

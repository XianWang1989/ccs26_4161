
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to collect results
    s = ''

    # Read and process each line
    for line in fh:
        # Remove newline characters
        s += line.strip()  # Using strip() to remove leading and trailing whitespace

# Output the final result
print(s)

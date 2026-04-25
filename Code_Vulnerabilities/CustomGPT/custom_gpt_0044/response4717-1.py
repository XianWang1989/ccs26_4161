
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store results
    s = ''
    # Read and process each line in the file
    for line in fh:
        # Remove newline characters and concatenate
        s += line.replace('\n', '')

# Print the result
print(s)

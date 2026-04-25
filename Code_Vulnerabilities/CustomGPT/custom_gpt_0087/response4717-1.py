
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''
    # Read and process the file line by line
    for line in fh:
        # Remove newline characters and accumulate the result
        s += line.strip()

# Print the final result
print(s)
